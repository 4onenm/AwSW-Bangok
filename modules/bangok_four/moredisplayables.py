from renpy.display.core import Displayable
from renpy.display.layout import Null

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