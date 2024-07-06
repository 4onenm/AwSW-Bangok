# pylint: disable=import-error
import renpy
import renpy.display.im as im
from renpy.display.behavior import ImageButton

clean_switch_displayables = dict(
    idle_image="image/ui/bangok/switchoff.png",
    hover_image = im.Recolor("image/ui/bangok/switchoff.png", 64, 64, 64),
    selected_idle_image="image/ui/bangok/switchon.png",
    selected_hover_image=im.Recolor("image/ui/bangok/switchon.png", 64, 64, 64),
)

def Switch(id, image=None, active_image=None, inactive_image=None, focus_mask=None, dim_inactive_image=None, **properties):
    if (image or active_image or inactive_image) is None:
        return ImageButton(clicked=renpy.store.MTSTogglePersistentBool(id), focus_mask=focus_mask, **clean_switch_displayables)

    if active_image is None:
        active_image = image
    if inactive_image is None:
        dim_inactive_image = True
        inactive_image = image

    if inactive_image is not None:
        if dim_inactive_image:
            inactive_image = im.Recolor(inactive_image, 128, 128, 128)

        idle = im.Composite((150,100),
            (0,0), "image/ui/bangok/switchoff.png",
            (15,15), inactive_image,
        )
    else:
        idle = "image/ui/bangok/switchoff.png"

    if active_image is not None:
        selected_idle = im.Composite((150,100),
            (0,0), "image/ui/bangok/switchon.png",
            (65,15), active_image,
        )
    else:
        selected_idle = "image/ui/bangok/switchon.png"

    displayables = dict(
        idle_image=idle,
        hover_image = im.Recolor(idle, 64, 64, 64),
        selected_idle_image=selected_idle,
        selected_hover_image=im.Recolor(selected_idle, 64, 64, 64),
    )

    displayables.update(properties)

    return ImageButton(
        clicked=renpy.store.MTSTogglePersistentBool(id),
        focus_mask=focus_mask,
        **displayables
    )



class _BangOkFetish():
    __slots__ = ('label', 'id', 'clean_label', 'image_clean', 'image', 'active_image', 'inactive_image')
    def __init__(self, label, id, clean_label='', image_clean=False, image=None, active_image=None, inactive_image=None):
        self.label = label
        self.id = id
        self.clean_label = clean_label
        self.image_clean = image_clean
        self.image = image
        self.active_image = active_image
        self.inactive_image = inactive_image

        self._cache = [None, None]

    def __eq__(self, __o):
        return self.id == __o.id

    def __hash__(self):
        return hash(self.id)

    def get_switch(self, clean=False):
        if self.image_clean or not clean:
            self._cache[0] = self._cache[0] or Switch(self.id, self.image, self.active_image, self.inactive_image, style='bangok_four_switch')
            return self._cache[0]
        else:
            self._cache[1] = self._cache[1] or Switch(self.id, style='bangok_four_switch')
            return self._cache[1]

    @property
    def images(self):
        return

_fetish_registy = set()

def register_fetish(label, id, clean_label='', image_clean=False, image=None, active_image=None, inactive_image=None):
    _fetish_registy.add(_BangOkFetish(label, id, clean_label, image_clean, image, active_image, inactive_image))


def fetish_count(clean=False):
    return len([f for f in _fetish_registy if f.clean_label or not clean])

def fetish_iter(clean=False):
    return [f for f in _fetish_registy if f.clean_label or not clean]





# Register base fetishes
register_fetish("Watersports", "bangok_watersports",
    clean_label="Hydration",
    image_clean=False,
    image="image/ui/bangok/icons/bangok_watersports.png",
)

register_fetish("Inflation", "bangok_inflation",
    clean_label="Balloons",
    image_clean=True,
    image="image/ui/bangok/icons/bangok_inflation.png",
)

register_fetish("Knotting", "bangok_knot",
    clean_label="Knot Tying",
    image_clean=True,
    image="image/ui/bangok/icons/bangok_knot.png",
)

register_fetish("Cloacas", "bangok_cloacas",
    clean_label="Motion",
    image_clean=True,
    active_image="image/ui/bangok/icons/bangok_cloacas_active.png",
    inactive_image="image/ui/bangok/icons/bangok_cloacas_inactive.png",
)

register_fetish("Cervix Penetration", "bangok_cervpen",
    image="image/ui/bangok/icons/bangok_cervpen.png"
)

register_fetish("Voyeurism", "bangok_voyeurism",
    clean_label="Investigation",
    image_clean=True,
    image="image/ui/bangok/icons/bangok_voyeurism.png"
)

register_fetish("Balls (WIP)", "bangok_balls",
    clean_label="Bowling",
    image_clean=True,
    image="image/ui/bangok/icons/bangok_balls.png",
)
