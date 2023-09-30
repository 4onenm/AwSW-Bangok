# pylint: disable=import-error
import renpy.exports
from renpy.exports import Displayable, render, Render, redraw, get_mouse_pos
import pygame
import math

# Initial parallax code thanks to Aquapaulo
#  https://github.com/aquapaulo/renpy-main-menu-parallax/blob/main/CODE.md
class TrackCursor(Displayable):
    def __init__(self, child, posxmin=0, posxmax=100, posymin=0, posymax=100):
        super(TrackCursor, self).__init__(style='transform')

        self.child = renpy.easy.displayable(child)
        self._duplicatable = self.child._duplicatable == True

        self.last_mouse_event_pos = None

        self.posxmin, self.posxmax = posxmin, posxmax
        self.posymin, self.posymax = posymin, posymax

    def _duplicate(self, args):

        if not self._duplicatable:
            return self

        rv = self._copy(args)
        rv.child = self.child._duplicate(args)

        return rv

    def render(self, width, height, st, at):
        mouse_x, mouse_y = get_mouse_pos()

        # (fractional part of relative mouse position) * (min-max range) + min
        x = math.modf(float(mouse_x)/renpy.config.screen_width)[0]*(self.posxmax - self.posxmin) + self.posxmin
        y = math.modf(float(mouse_y)/renpy.config.screen_height)[0]*(self.posymax - self.posymin) + self.posymin

        cr = render(self.child, width, height, st, at)
        rv = Render(width, height)
        rv.blit(cr, (x, y))

        return rv

    def event(self, ev, x, y, st):
        super(TrackCursor, self).event(ev, x, y, st)

        if ev.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN) and (self.last_mouse_event_pos != (x, y)):
            self.last_mouse_event_pos = (x, y)
            redraw(self, 0)

    def visit(self):
        return [ self.child ]