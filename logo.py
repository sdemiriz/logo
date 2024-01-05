import drawsvg as dw
import curve as c
import nord as n

d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 500, 500, fill=n.nord[1]))

start_minor = (350, 350)
size = (300, 300)
copy_offset = (0, -100)
offset = (0, -100)

c.Curve(
    drawing=d,
    start=start_minor,
    end=(start_minor[0] + size[0], start_minor[1] + size[1]),
    offset=offset,
    height_offset=-50,
    color=n.nord[10],
    debug=False,
)

c.Curve(
    drawing=d,
    start=(start_minor[0] + copy_offset[0], start_minor[1] + copy_offset[1]),
    end=(
        start_minor[0] + size[0] + copy_offset[0],
        start_minor[1] + size[1] + copy_offset[1],
    ),
    offset=offset,
    height_offset=-50,
    color=n.nord[10],
    debug=False,
)

start_major = (300, 300)
size = (400, -120)
copy_offset = (0, 350)
offset = (-25, 100)
c.Curve(
    drawing=d,
    start=start_major,
    end=(start_major[0] + size[0], start_major[1] + size[1]),
    offset=offset,
    height_offset=0,
    color=n.nord[9],
    debug=False,
)

c.Curve(
    drawing=d,
    start=(start_major[0] + copy_offset[0], start_major[1] + copy_offset[1]),
    end=(
        start_major[0] + copy_offset[0] + size[0],
        start_major[1] + copy_offset[1] + size[1],
    ),
    offset=offset,
    height_offset=0,
    color=n.nord[9],
    debug=False,
)


d.save_svg("logo.svg")
