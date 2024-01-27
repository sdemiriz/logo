import drawsvg as dw
import curve as c


class CenteredLogo:
    def draw_background(self, x_dimension, y_dimension, background_color):
        self.d.append(
            dw.Rectangle(
                x=0,
                y=0,
                width=x_dimension,
                height=y_dimension,
                fill=background_color,
            )
        )

    def draw_major_curves(
        self,
        drawing,
        start,
        end,
        thickness,
        offset,
        copy_offset,
        color,
        debug,
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

        c.Curve(
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
        drawing,
        start,
        end,
        thickness,
        offset,
        copy_offset,
        color,
        debug,
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

        c.Curve(
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

    def save_svg(self, filename):
        self.d.save_svg(f"img/{filename}.svg")

    def save_png(self, filename):
        self.d.save_png(f"img/{filename}.png")

    def __init__(
        self,
        canvas_dimensions: tuple[int, int],
        background_color: str,
        major_curve_color: str,
        minor_curve_color: str,
        curve_height: int,
        curve_width: int,
        curve_thickness: int,
        major_curve_separation: int,
        logo_scale: float,
        filename: str,
        debug: bool,
    ):
        self.canvas_dimensions = canvas_dimensions
        self.d = dw.Drawing(self.canvas_dimensions[0], self.canvas_dimensions[1])

        self.background_color = background_color
        self.major_curve_color = major_curve_color
        self.minor_curve_color = minor_curve_color
        self.logo_scale = logo_scale

        self.minor_curve_multiplier = 12
        self.major_curve_multiplier = 22

        self.curve_height = int(curve_height * self.logo_scale)
        self.curve_width = int(curve_width * self.logo_scale)
        self.thickness = int(curve_thickness * self.logo_scale)

        self.copy_offset_major = int(-major_curve_separation * self.logo_scale)
        self.copy_offset_minor = self.copy_offset_major + (
            (self.major_curve_multiplier + self.minor_curve_multiplier)
            * self.curve_height
        )

        self.logo_origin = (
            (self.canvas_dimensions[0] - self.curve_width) / 2,
            (
                self.canvas_dimensions[1]
                - (self.major_curve_multiplier * self.curve_height)
                - (self.copy_offset_major / 2)
            )
            / 2,
        )

        self.major_curve_size = (
            self.curve_width,
            self.major_curve_multiplier * self.curve_height,
        )
        self.major_curve_end = (
            self.logo_origin[0] + self.major_curve_size[0],
            self.logo_origin[1] + self.major_curve_size[1],
        )
        self.major_curve_offset = (0 * self.logo_scale, -100 * logo_scale)

        self.minor_curve_size = (
            self.curve_width,
            -self.minor_curve_multiplier * self.curve_height,
        )
        self.minor_curve_end = (
            self.logo_origin[0] + self.minor_curve_size[0],
            self.logo_origin[1] + self.minor_curve_size[1],
        )
        self.minor_curve_offset = (
            self.major_curve_offset[0],
            -self.major_curve_offset[1],
        )

        self.filename = filename
        self.debug = debug

        self.draw_background(
            self.canvas_dimensions[0],
            self.canvas_dimensions[1],
            self.background_color,
        )
        self.draw_major_curves(
            drawing=self.d,
            start=self.logo_origin,
            end=self.major_curve_end,
            thickness=self.thickness,
            offset=self.major_curve_offset,
            copy_offset=self.copy_offset_major,
            color=self.major_curve_color,
            debug=self.debug,
        )
        self.draw_minor_curves(
            drawing=self.d,
            start=self.logo_origin,
            end=self.minor_curve_end,
            thickness=self.thickness,
            offset=self.minor_curve_offset,
            copy_offset=self.copy_offset_minor,
            color=self.minor_curve_color,
            debug=self.debug,
        )
        self.save_svg()
        self.save_png()
