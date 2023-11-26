import renpy.exports
import renpy.display.im as im
import bangok_four.moredisplayables as md

PersistentConditionalDisplayable = md.PersistentConditionalDisplayable
PersistentConditionalComposite = md.PersistentConditionalComposite
RefHFlip = md.RefHFlip


class Expression:
    def __init__(
        self,
        name,
        composite,
        hflip="flip",  # type: Optional[Literal["flip", "ref"]]
        side_image_clipper=None,
    ):
        self.name = name
        self.composite = composite
        self.hflip = hflip
        self.side_image_clipper = side_image_clipper

    def load(self):
        renpy.exports.image(
            self.name,
            self.composite,
        )

        if self.hflip == "flip":
            renpy.exports.image(
                self.name + " flip",
                im.Flip(self.composite, horizontal=True),
            )
        elif self.hflip == "ref":
            renpy.exports.image(
                self.name + " ref",
                RefHFlip(self.name),
            )

    def load_side_image(self):
        if self.side_image_clipper is not None:
            renpy.exports.image(
                "side " + self.name,
                self.side_image_clipper(self.composite),
            )


def clip_anna_side_image(imagefile):
    return im.Flip(
        im.Scale(im.Crop(imagefile, (30, 35, 500, 600)), 250, 300),
        horizontal=True,
    )


def clip_bryce_side_image(imagefile):
    return im.Flip(
        im.Scale(im.Crop(imagefile, (400, 40, 500, 600)), 250, 300),
        horizontal=True,
    )


def clip_ipsum_side_image(composite):
    return im.Flip(
        im.Scale(im.Crop(composite, (100, 40, 500, 600)), 250, 300),
        horizontal=True,
    )


def clip_emera_side_image(composite):
    return im.Flip(
        im.Scale(im.Crop(composite, (0, 0, 500, 600)), 250, 300),
        horizontal=True,
    )


def clip_kalinth_side_image(composite):
    return im.Flip(
        im.Scale(im.Crop(composite, (80, 100, 500, 600)), 250, 300),
        horizontal=True,
    )


def clip_lorem_side_image(composite):
    return im.Flip(
        im.Scale(im.Crop(composite, (300, 0, 500, 500)), 250, 250),
        horizontal=True,
    )


def clip_sebastian_side_image(imagefile):
    return im.Flip(
        im.Scale(im.Crop(imagefile, (70, 0, 500, 600)), 250, 300),
        horizontal=True,
    )


expressions = [
    Expression(
        "anna bangok blush",
        "cr/anna_blush.png",
        side_image_clipper=clip_anna_side_image,
    ),
    Expression(
        "anna bangok orgasm",
        "cr/anna_orgasm.png",
        side_image_clipper=clip_anna_side_image,
    ),
    Expression(
        "anna bangok blushpalm",
        "cr/anna_blushpalm.png",
        side_image_clipper=clip_anna_side_image,
    ),
    Expression(
        "anna bangok lipbite",
        "cr/anna_lipbite.png",
        side_image_clipper=clip_anna_side_image,
    ),
    Expression(
        "bangok_four_bryce_underside_large dk",
        im.Recolor("cr/bryce_underside_large.png", 70, 70, 100, 255),
    ),
    Expression(
        "bryce normal bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_normal_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce brow bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_brow_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce flirty bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_flirty_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce laugh bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_laugh_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce smirk bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_smirk_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce stern bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_stern_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "bryce sad bangok foreleg flip",
        im.Composite(
            (1152, 969),
            (0, 0),
            "cr/bryce_sad_flip.png",
            (0, 0),
            "cr/bangok/bryce_foreleg.png",
        ),
        hflip=None,
    ),
    Expression(
        "damion normal bangok",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_normal.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
        ),
        hflip="ref",
    ),
    Expression(
        "damion face bangok",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_face.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
        ),
        hflip="ref",
    ),
    Expression(
        "damion arrogant bangok",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_arrogant.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
        ),
        hflip="ref",
    ),
    Expression(
        "damion normal bangok ws",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_normal.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
            (0, 0),
            "cr/bangok/damion_pen_ws.png",
        ),
        hflip="ref",
    ),
    Expression(
        "damion face bangok ws",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_face.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
            (0, 0),
            "cr/bangok/damion_pen_ws.png",
        ),
        hflip="ref",
    ),
    Expression(
        "damion arrogant bangok ws",
        PersistentConditionalComposite(
            (709, 827),
            (0, 0),
            "cr/damion_arrogant.png",
            (0, 0),
            PersistentConditionalDisplayable(
                "bangok_balls",
                "cr/bangok/damion_pen_ballz.png",
                None,
                "cr/bangok/damion_pen.png",
            ),
            (0, 0),
            "cr/bangok/damion_pen_ws.png",
        ),
        hflip="ref",
    ),
    Expression(
        "emera bangok blush b",
        "cr/bangok/emera_bangok_blush_b.png",
        side_image_clipper=clip_emera_side_image,
    ),
    Expression(
        "emera bangok orgasm b",
        "cr/bangok/emera_bangok_orgasm_b.png",
        side_image_clipper=clip_emera_side_image,
    ),
    Expression(
        "kalinth bangok normal blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok surprise",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok surprise blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok smile",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
            (175, 352),
            "cr/bangok/kalinth_smile.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok smile blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
            (175, 352),
            "cr/bangok/kalinth_smile.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok furtive blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (160, 312),
            "cr/bangok/kalinth_furtiveeyes.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok smilewink blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (175, 352),
            "cr/bangok/kalinth_smile.png",
            (210, 297),
            "cr/bangok/kalinth_leftclosedeye.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok eyesclosed blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (157, 297),
            "cr/bangok/kalinth_closedeyes.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok smile eyesclosed blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
            (175, 352),
            "cr/bangok/kalinth_smile.png",
            (157, 297),
            "cr/bangok/kalinth_closedeyes.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "kalinth bangok smile eyeslidded blush",
        im.Composite(
            (1134, 950),
            (0, 0),
            "cr/kalinth_normal.png",
            (161, 282),
            "cr/bangok/kalinth_browrelaxed.png",
            (175, 352),
            "cr/bangok/kalinth_smile.png",
            (157, 297),
            "cr/bangok/kalinth_liddedeyes.png",
            (134, 321),
            "cr/bangok/kalinth_blush.png",
        ),
        side_image_clipper=clip_kalinth_side_image,
    ),
    Expression(
        "lorem happy bangok shy",
        "cr/bangok/lorem_happy+blush.png",
        side_image_clipper=clip_lorem_side_image,
    ),
    Expression(
        "lorem happy bangok shy2",
        "cr/bangok/lorem_happy2+blush.png",
        side_image_clipper=clip_lorem_side_image,
    ),
    Expression(
        "lorem bangok aheago1",
        "cr/bangok/lorem_aheago1.png",
        side_image_clipper=clip_lorem_side_image,
    ),
    Expression(
        "lorem bangok aheago2",
        "cr/bangok/lorem_aheago2.png",
        side_image_clipper=clip_lorem_side_image,
    ),
    Expression(
        "lorem normal bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem happy bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem sad bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem relieved bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_relieved.png",
            (0, 0),
            "cr/bangok/lorem_penis_armcovered.png",
        ),
    ),
    Expression(
        "lorem shy bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem think bangok erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem normal bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem happy bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem sad bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem relieved bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_relieved.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis_armcovered.png",
        ),
    ),
    Expression(
        "lorem shy bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem think bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem blush bangok bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_blush.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem happy bangok shy bulge erect",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/bangok/lorem_Happy+blush.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_penis.png",
        ),
    ),
    Expression(
        "lorem normal bangok cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem happy bangok cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem sad bangok cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem shy bangok cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem think bangok cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem normal bangok pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem happy bangok pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem sad bangok pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem shy bangok pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem think bangok pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem normal bangok bulge cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem happy bangok bulge cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem sad bangok bulge cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem shy bangok bulge cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem think bangok bulge cumleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_cumleak.png",
        ),
    ),
    Expression(
        "lorem normal bangok bulge pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem happy bangok bulge pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem sad bangok bulge pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem shy bangok bulge pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem think bangok bulge pissleak",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (0, 0),
            "cr/bangok/lorem_bulge.png",
            (0, 0),
            "cr/bangok/lorem_pen_pissleak.png",
        ),
    ),
    Expression(
        "lorem normal bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_normal.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem happy bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_happy.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem sad bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_sad.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem relieved bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_relieved.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem shy bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_shy.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem think bangok peek",
        im.Composite(
            (1240, 650),
            (0, 0),
            "cr/lorem_think.png",
            (626, 579),
            "cr/lorem_bangok_peek.png",
        ),
    ),
    Expression(
        "lorem bangok hidepeek",
        "cr/lorem_bangok_hidepeek.png",
        side_image_clipper=clip_lorem_side_image,
    ),
    Expression(
        "ipsum look bangok",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_look.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum normal bangok blush",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_normal_blush.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum happy bangok blush",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_happy_blush.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum normal bangok heady",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_heady.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum happy bangok heady",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_heady_grin.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum normal bangok erect wrapped",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_normal.png",
            (214, 684),
            "cr/ipsum_bangok_pen.png",
        ),
    ),
    Expression(
        "ipsum happy bangok erect wrapped",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_happy.png",
            (214, 684),
            "cr/ipsum_bangok_pen.png",
        ),
    ),
    Expression(
        "ipsum sad bangok erect wrapped",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (214, 684),
            "cr/ipsum_bangok_pen.png",
        ),
    ),
    Expression(
        "ipsum think bangok erect wrapped",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_think.png",
            (214, 684),
            "cr/ipsum_bangok_pen.png",
        ),
    ),
    Expression(
        "ipsum normal bangok briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_normal.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum normal bangok blush briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_normal_blush.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum normal bangok aheago briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_aheago_1_drop.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
        side_image_clipper=clip_ipsum_side_image,
    ),
    Expression(
        "ipsum happy bangok briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_happy.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum happy bangok blush briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_happy_blush.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum sad bangok briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum think bangok briefs",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_think.png",
            (0, 0),
            "cr/bangok/ipsum_briefs.png",
        ),
    ),
    Expression(
        "ipsum normal bangok briefs touch",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_normal.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum normal bangok heady briefs touch",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_heady.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum happy bangok briefs touch",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_happy.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum sad bangok briefs touch",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum normal bangok briefs touch glow",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_normal.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_glow.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum normal bangok blush briefs touch glow",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_normal_blush.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_glow.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum happy bangok briefs touch glow",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_happy.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_glow.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum sad bangok briefs touch glow",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_glow.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
        ),
    ),
    Expression(
        "ipsum happy bangok blush briefs touch glow",
        im.Composite(
            (650, 800),
            (0, 0),
            "cr/ipsum_sad.png",
            (0, 0),
            "cr/bangok/ipsum_happy_blush.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_touch.png",
            (0, 0),
            "cr/bangok/ipsum_briefs_glow.png",
        ),
    ),
    Expression(
        "sebastian normal b dk",
        im.Recolor("cr/sebastian_normal_b.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian normal dk",
        im.Recolor("cr/sebastian_normal.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian shy dk",
        im.Recolor("cr/sebastian_shy.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian shy b dk",
        im.Recolor("cr/sebastian_shy_b.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian drop dk",
        im.Recolor("cr/sebastian_drop.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian drop b dk",
        im.Recolor("cr/sebastian_drop_b.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian smile dk",
        im.Recolor("cr/sebastian_smile.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian smile b dk",
        im.Recolor("cr/sebastian_smile_b.png", 70, 70, 100, 255),
    ),
    Expression(
        "sebastian shy b sleep",
        "cr/sebastian_shy_b_sleep.png",
        side_image_clipper=clip_sebastian_side_image,
    ),
    Expression(
        "sebastian shy b sleep dk",
        im.Recolor("cr/sebastian_shy_b_sleep.png", 70, 70, 100, 255),
        side_image_clipper=clip_sebastian_side_image,
    ),
]


def load_all_expressions():
    for e in expressions:
        print("Loading BangOk expression: " + e.name)
        e.load()


def load_all_side_images():
    for e in expressions:
        e.load_side_image()
