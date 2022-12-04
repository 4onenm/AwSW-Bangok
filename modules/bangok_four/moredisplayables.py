from renpy.display.core import Displayable
from renpy.display.layout import Null

import renpy.easy
import renpy

class PersistentConditionalDisplayable(Displayable):
    __slots__ = ('persistent_attribute', 'true_displayable', 'false_displayable', 'current_value')
    nosave = ['current_value']

    def after_setstate(self):
        self.current_value = None

    def __init__(self, persistent_attribute, true_displayable=None, false_displayable=None):
        super(PersistentConditionalDisplayable, self).__init__()

        if true_displayable is None and false_displayable is None:
            raise ValueError("%s requires at least one of `true_displayable`, `false_displayable`"%(self.__class__,))

        self.persistent_attribute = persistent_attribute
        self.true_displayable = renpy.easy.displayable_or_none(true_displayable) if true_displayable is not None else Null() 
        self.false_displayable = renpy.easy.displayable_or_none(false_displayable) if false_displayable is not None else Null()
        self.current_value = None

    def _duplicate(self, args):
        if not self._duplicatable:
            return self

        rv = self._copy(args)
        rv.true_displayable = self.true_displayable._duplicate(args)
        rv.false_displayable = self.false_displayable._duplicate(args)

        return rv

    def _in_current_store(self):
        new_true = self.true_displayable._in_current_store()
        new_false = self.false_displayable._in_current_store()

        if (new_true is self.true_displayable) and (new_false is self.false_displayable):
            return self

        rv = self._copy()
        rv.true_displayable = new_true
        rv.false_displayable = new_false

        return rv

    def get_current_child(self):
        return self.true_displayable if self.current_value else self.false_displayable

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
        return [self.false_displayable, self.true_displayable]

    def per_interact(self):
        old_value = self.current_value
        self.current_value = getattr(renpy.store.persistent, self.persistent_attribute, False)
        if self.current_value != old_value:
            renpy.display.render.redraw(self, 0)

    def predict_one(self):
        renpy.display.predict.displayable(self.get_current_child())

    def _clear(self):
        self.true_displayable = Null()
        self.false_displayable = Null()