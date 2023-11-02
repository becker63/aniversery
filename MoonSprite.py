from asciimatics.effects import Sprite
from asciimatics.renderers import StaticRenderer


def text_circle(rad, ch="*"):
    chars = []
    xscale = 4.2
    # Maximum diameter, plus a little padding
    width = 3 + int(0.5 + xscale * rad)

    rad2 = rad**2
    for y in range(-rad, rad + 1):
        # Find width at this height
        x = int(0.5 + xscale * (rad2 - y**2) ** 0.5)
        s = ch * x
        chars.append(s.center(width))
    return "\n".join(chars)


# moon_defualt = """
#  ,MMM8&&&.
# MMMM88&&&&&
# MMMM88&&&&&&&
# MMM88&&&&&&&&
# MMM88&&&&&&&&
#'MMM88&&&&&&'
#  'MMM8&&&'
#                   """

# moon_defualt = text_circle(10)


class Moon(Sprite):
    """
    Moon
    """

    def __init__(self, screen, path, start_frame=0, stop_frame=0):
        super().__init__(
            screen,
            renderer_dict={
                "default": StaticRenderer(
                    images=[
                        text_circle(
                            int((screen.width * 0.4) + (screen.height * 1.2)) // 10
                        )
                    ]
                ),
            },
            path=path,
            start_frame=start_frame,
            stop_frame=stop_frame,
        )
