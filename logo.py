import drawsvg as dw

nord = [
    "#2e3440",
    "#3b4252",
    "#434c5e",
    "#4c566a",
    "d8dee9",
    "#e5e9f0",
    "#eceff4",
    "#8fbcbb",
    "#88c0d0",
    "#81a1c1",
    "#5e81ac",
    "#bf616a",
    "#d08770",
    "#ebc88b",
    "#a3be8c",
    "#b48ead",
]

type coord = tuple[float, float]


class Curve:
    def __init__(self, drawing: dw.Drawing, start: coord, end: coord, offset: coord, translate: coord, color: str, debug: bool):
        self.start = start
        self.end = end
        self.offset = offset
        self.color = color
        self.translate = translate
        self.stroke_width = 30
        self.debug = debug

        self.handle1 = (self.start[0] + self.offset[0], self.start[1] + self.offset[1])
        self.handle2 = (self.end[0] - self.offset[0], self.end[1] - self.offset[1])

        self.path = dw.Path(
            stroke=self.color,
            fill="none",
            stroke_width=self.stroke_width,
            transform=f"translate({self.translate[0]}, {self.translate[1]})",
        )
        self.path.M(*self.start).C(*self.handle1, *self.handle2, *self.end)

        drawing.append(self.path)

        if self.debug:
            drawing.append(dw.Circle(*self.handle1, 5, stroke="#ff0000", fill="#ff0000"))
            drawing.append(dw.Circle(*self.handle2, 5, stroke="#ff0000", fill="#ff0000"))



d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 500, 500, fill=nord[1]))


r = dw.Rectangle(125, 80, 250, 200)

start = (400, 50)
mid1 = (100, 250)
offset1 = (0, 150)
psm1 = (start[0] + offset1[0], start[1] + offset1[1])
psm2 = (mid1[0] - offset1[0], mid1[1] - offset1[1])

Curve(d, start, mid1, offset1, (0, 0), nord[15], True)

r2 = dw.Rectangle(125, 175, 250, 300)

mid2 = (100, 150)
end = (400, 500)
offset2 = (0, 175)
psm3 = (mid2[0] + offset2[0], mid2[1] + offset2[1])
psm4 = (end[0] - offset2[0], end[1] - offset2[1])

Curve(d, mid2, end, offset2, (0, 0), nord[14], True)

d.save_svg("logo.svg")
