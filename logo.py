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


class Curve:
    def __init__(
        self,
        drawing: dw.Drawing,
        start: tuple,
        end: tuple,
        offset: tuple,
        translate: tuple,
        color: str,
        rect_offset: int,
        debug: bool,
    ):
        self.start = start
        self.end = end
        self.offset = offset
        self.color = color
        self.rect_offset = rect_offset
        self.translate = translate
        self.stroke_width = 30
        self.debug = debug

        self.handle1 = (self.start[0] - self.offset[0], self.start[1] - self.offset[1])
        self.handle2 = (self.end[0] + self.offset[0], self.end[1] + self.offset[1])

        r = dw.Rectangle(
            min(self.start[0], self.end[0]) + self.rect_offset,
            0,
            abs(self.start[0] - self.end[0]) - 2 * self.rect_offset,
            500,
            stroke="#ff0000",
            fill="none",
        )

        drawing.append(r)

        clip = dw.ClipPath()
        clip.append(r)

        self.path = dw.Path(
            stroke=self.color,
            fill="none",
            stroke_width=self.stroke_width,
            transform=f"translate({self.translate[0]}, {self.translate[1]})",
            clip_path=clip,
        )
        self.path.M(*self.start).C(*self.handle1, *self.handle2, *self.end)

        drawing.append(self.path)

        if self.debug:
            drawing.append(
                dw.Circle(
                    self.handle1[0] + self.translate[0],
                    self.handle1[1] + self.translate[1],
                    5,
                    stroke="#ff0000",
                    fill="#ff0000",
                )
            )
            drawing.append(
                dw.Circle(
                    self.handle2[0] + self.translate[0],
                    self.handle2[1] + self.translate[1],
                    5,
                    stroke="#ff0000",
                    fill="#ff0000",
                )
            )


d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 500, 500, fill=nord[1]))


r = dw.Rectangle(125, 80, 250, 200)

start = (100, 250)
end = (400, 50)
offset1 = (0, 150)
Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset1,
    translate=(0, 0),
    rect_offset=30,
    color=nord[15],
    debug=False,
)

r2 = dw.Rectangle(125, 175, 250, 300)

start = (100, 150)
end = (400, 400)
offset = (-100, 50)
Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    translate=(0, 40),
    rect_offset=30,
    color=nord[14],
    debug=False,
)

d.save_svg("logo.svg")
