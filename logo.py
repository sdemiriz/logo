import drawsvg as dw
import curve as c
import nord as n

d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 500, 500, fill=n.nord[1]))

start = (100, 200)
end = (start[0] + 300, start[1] + 300)
offset = (0, -100)
c.Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    height_offset=-50,
    color=n.nord[10],
    debug=False,
)

start = (100, 100)
end = (start[0] + 300, start[1] + 300)
offset = (0, -100)
c.Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    height_offset=-50,
    color=n.nord[10],
    debug=False,
)

start = (100, 150)
end = (start[0] + 300, start[1] - 150)
offset = (-25, 100)
c.Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    height_offset=0,
    color=n.nord[9],
    debug=False,
)

start = (100, 500)
end = (start[0] + 300, start[1] - 150)
offset = (-25, 100)
c.Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    height_offset=0,
    color=n.nord[9],
    debug=False,
)


d.save_svg("logo.svg")
