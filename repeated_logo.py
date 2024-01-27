import drawsvg as dw
import curve as c


class RepeatedLogo:
    def draw_background(
        self,
        x_dimension,
        y_dimension,
        background_color,
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

    def draw_repeats(self):
        self.x_offset, self.y_offset = self.pattern_repeat

        x, y = 0, 0
        while x <= self.canvas_dimensions[0] + 1000:
            while y <= self.canvas_dimensions[1] + 1000:
                self.logo_origin = (x - self.x_offset / 2, y - self.y_offset / 2)
                self.major_curve_end = (
                    self.logo_origin[0] + self.major_curve_size[0],
                    self.logo_origin[1] + self.major_curve_size[1],
                )
                self.minor_curve_end = (
                    self.logo_origin[0] + self.minor_curve_size[0],
                    self.logo_origin[1] + self.minor_curve_size[1],
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

                self.logo_origin = (x, y)
                self.major_curve_end = (
                    self.logo_origin[0] + self.major_curve_size[0],
                    self.logo_origin[1] + self.major_curve_size[1],
                )
                self.minor_curve_end = (
                    self.logo_origin[0] + self.minor_curve_size[0],
                    self.logo_origin[1] + self.minor_curve_size[1],
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

                y += self.y_offset

            y = 0
            x += self.x_offset

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
        separation: int,
        major_curve_multiplier: int,
        minor_curve_multiplier: int,
        logo_scale: float,
        pattern_repeat: tuple[int, int],
        filename: str,
        debug: bool,
    ):
        # Define output name and use of debug mode
        self.filename = filename
        self.debug = debug

        # Set up image and color background
        self.canvas_dimensions = canvas_dimensions
        self.d = dw.Drawing(
            self.canvas_dimensions[0],
            self.canvas_dimensions[1],
        )

        self.background_color = background_color
        self.draw_background(
            self.canvas_dimensions[0],
            self.canvas_dimensions[1],
            self.background_color,
        )

        # Ingest curve related parameters
        self.major_curve_color = major_curve_color
        self.minor_curve_color = minor_curve_color
        self.minor_curve_multiplier = minor_curve_multiplier
        self.major_curve_multiplier = major_curve_multiplier
        self.logo_scale = logo_scale
        self.pattern_repeat = pattern_repeat

        self.curve_height = int(curve_height * self.logo_scale)
        self.curve_width = int(curve_width * self.logo_scale)
        self.thickness = int(curve_thickness * self.logo_scale)

        self.copy_offset_major = int(-separation * self.logo_scale)
        self.copy_offset_minor = self.copy_offset_major + (
            (self.major_curve_multiplier + self.minor_curve_multiplier)
            * self.curve_height
        )

        self.major_curve_size = (
            self.curve_width,
            self.major_curve_multiplier * self.curve_height,
        )
        self.major_curve_offset = (0 * self.logo_scale, -100 * logo_scale)

        self.minor_curve_size = (
            self.curve_width,
            -self.minor_curve_multiplier * self.curve_height,
        )
        self.minor_curve_offset = (
            self.major_curve_offset[0],
            -self.major_curve_offset[1],
        )

        self.draw_repeats()
        self.save_svg(self.filename)
        self.save_png(self.filename)
