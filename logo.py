import drawsvg as dw
import curve as c
import nord


class Curve:
    def __init__(
        self,
        drawing: dw.Drawing,
        start: tuple,
        end: tuple,
        offset: tuple,
        scale: tuple,
        height_offset: int,
        color: str,
        debug: bool,
    ):
        self.start = start
        self.end = end
        self.offset = offset
        self.color = color
        self.scale = scale
        self.height_repeats = 50
        self.height_offset = height_offset
        self.stroke_width = 2
        self.debug = debug

        self.handle1 = (self.start[0] - self.offset[0], self.start[1] - self.offset[1])
        self.handle2 = (self.end[0] + self.offset[0], self.end[1] + self.offset[1])

        for i in range(self.height_repeats):
            self.path = dw.Path(
                stroke=self.color,
                fill="none",
                stroke_width=self.stroke_width,
                transform=f"\
                    translate(0, {i + self.height_offset}) \
                    scale({self.scale[0]}, {self.scale[1]})",
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


d = dw.Drawing(1000, 1000, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 1000, 1000, fill=nord[1]))

start = (100, 200)
end = (start[0] + 300, start[1] + 300)
offset = (0, -100)
c.Curve(
    drawing=d,
    start=start,
    end=end,
    offset=offset,
    scale=(1, 1),
    height_offset=-50,
    color=nord[10],
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
    scale=(1, 1),
    height_offset=-50,
    color=nord[10],
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
    scale=(1, 1),
    height_offset=0,
    color=nord[9],
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
    scale=(1, 1),
    height_offset=0,
    color=nord[9],
    debug=False,
)


d.save_svg("logo.svg")
