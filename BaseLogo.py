import drawsvg as dw
import curve as c


class BaseLogo:
    def draw_background(
        self,
        x_dimension: int,
        y_dimension: int,
        background_color: str,
    ):
        self.d.append(
            dw.Rectangle(
                x=0,
                y=0,
                width=x_dimension,
                height=y_dimension,
                fill=background_color,
            )
        )

    def draw_curve(
        self,
        drawing: dw.Drawing,
        start: tuple[int, int],
        end: tuple[int, int],
        thickness: int,
        offset: int,
        color: str,
        debug: bool,
    ):
        c.Curve(
            drawing=drawing,
            start=start,
            end=end,
            thickness=thickness,
            offset=offset,
            color=color,
            debug=debug,
        )

    def draw_major_curves(
        self,
        drawing: dw.Drawing,
        start: tuple[int, int],
        end: tuple[int, int],
        thickness: int,
        offset: int,
        copy_offset: int,
        color: str,
        debug: bool,
    ):
        self.draw_curve(
            drawing=drawing,
            start=start,
            end=end,
            thickness=thickness,
            offset=offset,
            color=color,
            debug=debug,
        )

        self.draw_curve(
            drawing=drawing,
            start=(
                start[0],
                start[1] + copy_offset,
            ),
            end=(
                end[0],
                end[1] + copy_offset,
            ),
            thickness=thickness,
            offset=offset,
            color=color,
            debug=debug,
        )

    def draw_minor_curves(
        self,
        drawing: dw.Drawing,
        start: tuple[int, int],
        end: tuple[int, int],
        thickness: int,
        offset: int,
        copy_offset: int,
        color: str,
        debug: bool,
    ):
        self.draw_curve(
            drawing=drawing,
            start=start,
            end=end,
            thickness=thickness,
            offset=offset,
            color=color,
            debug=debug,
        )

        self.draw_curve(
            drawing=drawing,
            start=(
                start[0],
                start[1] + copy_offset,
            ),
            end=(
                end[0],
                end[1] + copy_offset,
            ),
            thickness=thickness,
            offset=offset,
            color=color,
            debug=debug,
        )

    def save_svg(self, filename: str):
        self.d.save_svg(f"img/{filename}.svg")

    def save_png(self, filename: str):
        self.d.save_png(f"img/{filename}.png")
