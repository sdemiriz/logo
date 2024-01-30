import drawsvg as dw
import BaseLogo as base


class RepeatedLogo(base.BaseLogo):
    def draw_repeats(self, pattern_repeat):
        self.x_offset, self.y_offset = pattern_repeat

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

        # Calculate shared curve parameters
        self.curve_height = int(curve_height * self.logo_scale)
        self.curve_width = int(curve_width * self.logo_scale)
        self.thickness = int(curve_thickness * self.logo_scale)

        # Calculate values relating to the two halves of the logo
        self.copy_offset_major = int(-separation * self.logo_scale)
        self.copy_offset_minor = self.copy_offset_major + (
            (self.major_curve_multiplier + self.minor_curve_multiplier)
            * self.curve_height
        )

        # Calculate major curve parameters
        self.major_curve_size = (
            self.curve_width,
            self.major_curve_multiplier * self.curve_height,
        )
        self.major_curve_offset = (0 * self.logo_scale, -100 * logo_scale)

        # Calculate minor curve parameters
        self.minor_curve_size = (
            self.curve_width,
            -self.minor_curve_multiplier * self.curve_height,
        )
        self.minor_curve_offset = (
            self.major_curve_offset[0],
            -self.major_curve_offset[1],
        )

        # Draw
        self.draw_repeats(pattern_repeat=pattern_repeat)

        # Save to file(s)
        self.save_svg(filename=self.filename)
        self.save_png(filename=self.filename)
