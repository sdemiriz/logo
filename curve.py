import drawsvg as dw


class Curve:
    def __init__(
        self,
        drawing: dw.Drawing,
        start: tuple,
        end: tuple,
        thickness: int,
        offset: tuple,
        scale: tuple = (1, 1),
        color: str = "#ff0000",
        debug: bool = False,
    ):
        self.start = start
        self.end = end
        self.offset = offset
        self.color = color
        self.scale = scale
        self.thickness = thickness
        self.stroke_width = 2
        self.debug = debug

        self.handle1 = (self.start[0] - self.offset[0], self.start[1] - self.offset[1])
        self.handle2 = (self.end[0] + self.offset[0], self.end[1] + self.offset[1])

        for i in range(self.thickness):
            self.path = dw.Path(
                stroke=self.color,
                fill="none",
                stroke_width=self.stroke_width,
                transform=f"\
                    translate(0, {i}) \
                    scale({self.scale[0]}, {self.scale[1]})",
            )
            self.path.M(*self.start).C(*self.handle1, *self.handle2, *self.end)
            drawing.append(self.path)

        if self.debug:
            self.path = dw.Path(
                stroke="#ff0000",
                fill="none",
                stroke_width=self.stroke_width,
                transform=f"scale({self.scale[0]}, {self.scale[1]})",
            )
            self.path.M(*self.start).C(*self.handle1, *self.handle2, *self.end)
            drawing.append(self.path)

            drawing.append(
                dw.Circle(
                    self.handle1[0],
                    self.handle1[1],
                    5,
                    stroke="#ff0000",
                    fill="#ff0000",
                )
            )
            drawing.append(
                dw.Circle(
                    self.handle2[0],
                    self.handle2[1],
                    5,
                    stroke="#ff0000",
                    fill="#ff0000",
                )
            )
