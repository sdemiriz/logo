import drawsvg as dw
import curve as c
import nord as n

WIDTH = 1000
HEIGHT = 1000
d = dw.Drawing(WIDTH, HEIGHT, id_prefix="pic")
d.append(dw.Rectangle(0, 0, WIDTH, HEIGHT, fill=n.nord[1]))

minor_curve_multiplier = 12
major_curve_multiplier = 22
curve_height = 10
curve_width = 300

curve_left = (WIDTH - curve_width) / 2

start_major = (curve_left, 400)
size = (curve_width, major_curve_multiplier * curve_height)
copy_offset = -80
offset = (0, -100)

c.Curve(
    drawing=d,
    start=start_major,
    end=(start_major[0] + size[0], start_major[1] + size[1]),
    offset=offset,
    color=n.nord[10],
    debug=False,
)

c.Curve(
    drawing=d,
    start=(start_major[0], start_major[1] + copy_offset),
    end=(
        start_major[0] + size[0],
        start_major[1] + size[1] + copy_offset,
    ),
    offset=offset,
    color=n.nord[10],
    debug=False,
)

start_minor = (curve_left, 400)
size = (curve_width, -minor_curve_multiplier * curve_height)
copy_offset = 250
offset = (-25, 100)
c.Curve(
    drawing=d,
    start=start_minor,
    end=(start_minor[0] + size[0], start_minor[1] + size[1]),
    offset=offset,
    color=n.nord[9],
    debug=False,
)

c.Curve(
    drawing=d,
    start=(start_minor[0], start_minor[1] + copy_offset),
    end=(
        start_minor[0] + size[0],
        start_minor[1] + copy_offset + size[1],
    ),
    offset=offset,
    height_offset=10,
    color=n.nord[9],
    debug=False,
)


d.save_svg("logo.svg")
