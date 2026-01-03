# pylint: disable=import-error
from renpy.display.core import Displayable
from renpy.display.layout import Null
from renpy.display import im

import renpy.easy
import renpy


try:
    import jz_magmalink.extras.layeredimage as layeredimage
except:
    print("WARNING: Magmalink version does not include `layeredimage`.\n\tFalling back to a copy contained in BangOk.\n\tThis fallback may be removed in a future version.")
    import bangok_four.layeredimage_fallback as layeredimage

class PersistentConditionalDisplayable(Displayable):
    __slots__ = ('conditions', 'children', 'child')
    nosave = ['child']

    def after_setstate(self):
        self.child = self.children[0]

    def __init__(self, *args, **kwargs):
        super(PersistentConditionalDisplayable, self).__init__()

        if len(args) & 1 == 1:
            raise ValueError("%s requires an even number of arguments."%(self.__class__,))

        self.conditions = tuple(((arg,) if isinstance(arg,basestring) else () if arg is None else arg for arg in args[0::2]))
        self.children = tuple((renpy.easy.displayable(d) if d is not None else Null() for d in args[1::2]))
        self.child = None

    def _duplicate(self, args):
        if not self._duplicatable:
            return self

        rv = self._copy(args)
        rv.children = tuple((c._duplicate(args) for c in self.children))
        rv.child = None

        return rv

    def _in_current_store(self):
        new_children = tuple((c._in_current_store() for c in self.children))

        if all((c is old for c, old in zip(new_children, self.children))):
            return self

        rv = self._copy()
        rv.children = new_children
        rv.child = None

        return rv

    def get_current_child(self, update=False):
        if update or self.child is None:
            for condition, child in zip(self.conditions, self.children):
                if all(getattr(renpy.store.persistent, attr, False) for attr in condition):
                    self.child = child
                    return child
            raise ValueError("No child matched PersistentConditionalDisplayable current conditions: %s"%(self.conditions,))

        return self.child

    def render(self, width, height, st, at):
        return self.get_current_child().render(width,height,st,at)

    def event(self, ev, x, y, st):
        return self.get_current_child().event(ev, x, y, st)

    def set_style_prefix(self, prefix, root):
        super().set_style_prefix(prefix, root)

        for i in self.visit():
            i.set_style_prefix(prefix, root)

    def get_placement(self):
        return self.get_current_child().get_placement()

    def visit(self):
        return self.children

    def per_interact(self):
        old_value = self.child
        self.get_current_child(update=True) # Sets self.child
        if self.child != old_value:
            renpy.display.render.redraw(self, 0)

    def predict_one(self):
        renpy.display.predict.displayable(self.get_current_child())

    def _clear(self):
        self.child = None
        self.children = ()
        self.conditions = ()

def PersistentConditionalLayer(*args, **kwargs):
    return layeredimage.Always(PersistentConditionalDisplayable(*args), **kwargs)

def PersistentConditionalComposite(size, *args, **kwargs):
    if len(args) & 1 != 0:
        raise Exception("Composite requires an odd number of arguments.")

    positions = args[0::2]
    children = args[1::2]

    conditions = []
    for i, child in enumerate(children):
        if isinstance(child, PersistentConditionalDisplayable):
            conditions.append((i, child.conditions, child.children))

    if len(conditions) == 0:
        return im.Composite(size, *args, **kwargs)
    elif len(conditions) == 1:
        null = Null()
        i, conds, subchildren = conditions[0]
        composites = []
        for subchild in subchildren:
            if isinstance(subchild, Null):
                these_positions = list(positions[:i]) + list(positions[i+1:])
                these_children = list(children[:i]) + list(children[i+1:])
            else:
                these_positions = positions
                these_children = list(children)
                these_children[i] = subchild
            composite = im.Composite(size, *sum(zip(these_positions, these_children), ()), **kwargs)
            composites.append(composite)

        return PersistentConditionalDisplayable(*sum(zip(conds, composites), ()))
    else:
        raise NotImplementedError("PersistentConditionalComposite does not support more than one PersistentConditionalDisplayable child.")

def PersistentConditionalFlip(d, **kwargs):
    if isinstance(d, renpy.display.image.ImageReference):
        d.find_target()
        d = d.target

    if isinstance(d, PersistentConditionalDisplayable):
        return PersistentConditionalDisplayable(*sum(zip(d.conditions, (im.Flip(child, **kwargs) for child in d.children)), ()))
    else:
        return im.Flip(d, **kwargs)

def RefHFlip(arg, horizontal=True, **kwargs):
    if isinstance(arg, basestring):
        if '/' in arg:
            arg = renpy.display.im.image(arg)
        else:
            arg = renpy.display.image.ImageReference(arg)

    return PersistentConditionalFlip(arg, horizontal=horizontal, **kwargs)

class PersistentRecolorDisplayable(im.ImageBase):
    __slots__ = ('persistent', 'default', 'image', 'raw_color')
    nosave = [ 'raw_color' ]

    def __init__(self, image, persistent, default,**properties):
        image = im.image(image)
        default = renpy.easy.color(default)
        super(PersistentRecolorDisplayable,self).__init__(im,persistent,default,**properties)
        self.image = image
        self.persistent = persistent
        self.default = default
        self.raw_color = None

    def __hash__(self):
        return hash(self.persistent)

    def get_hash(self):
        return self.image.get_hash()

    def find_color(self, update=True):
        try:
            col = renpy.easy.color(getattr(renpy.store.persistent, self.persistent, self.default))
        except Exception as e:
            raise Exception("In PersistentRecolorDisplayable %r: %r" % (self.persistent, e))
        
        if self.raw_color == col:
            return False

        if not update:
            return True

        # Color changed, bust cache and redraw.
        self.raw_color = col

        ce = im.cache.cache.get(self, None)
        if ce is not None:
            with im.cache.lock:
                im.cache.kill(ce)
        renpy.display.render.redraw(self,0)

        return True

    def current_color(self):
        if self.raw_color:
            return self.raw_color
        try:
            return renpy.easy.color(getattr(renpy.store.persistent, self.persistent, None) or self.default)
        except:
            pass # Eat exceptions so we can put _something_ on the screen.
        # Bright magenta error color
        return renpy.easy.color("#ff00dc")

    def load(self):
        surf = im.cache.get(self.image)
        rv = renpy.display.pgrender.surface(surf.get_size(), True)
        renpy.display.module.linmap(surf, rv, *self.current_color())
        return rv

    def _duplicate(self, args):
        rv = self._copy(args)
        rv.raw_color = None
        return rv

    def _hide(self, st, at, kind):
        return self.image._hide(st, at, kind)

    def set_transform_event(self, event):
        return self.image.set_transform_event(event)

    def event(self, ev, x, y, st):
        return self.image.event(ev, x, y, st)

    def render(self, width, height, st, at):
        image = im.cache.get(self)
        texture = renpy.display.draw.load_texture(image)
        w, h = image.get_size()
        rv = renpy.display.render.Render(w, h)
        rv.blit(texture, (0,0))
        return rv

    def get_placement(self):
        return self.image.get_placement()

    def visit(self):
        return [self.image]

    def predict_one(self):
        return renpy.display.predict.image(self.image)
    
    def predict_files(self):
        return self.image.predict_files()

    def per_interact(self):
        self.find_color(update=True)