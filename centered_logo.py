import drawsvg as dw
import curve as c
import nord as n


class CenteredLogo:
    def __init__(
        self,
        canvas_dimensions: tuple[int, int],
        background_color: str,
        major_curve_color: str,
        minor_curve_color: str,
        logo_scale: float,
        filename: str,
    ):
        self.canvas_dimensions = canvas_dimensions

        self.background_color = background_color
        self.major_curve_color = major_curve_color
        self.minor_curve_color = minor_curve_color

        self.logo_scale = logo_scale

        self.minor_curve_multiplier = 12
        self.major_curve_multiplier = 22

        self.curve_height = int(10 * self.logo_scale)
        self.curve_width = int(300 * self.logo_scale)
        self.thickness = int(42 * self.logo_scale)

        self.copy_offset_major = int(-84 * self.logo_scale)
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
            self.major_curve_offset[1] * -1,
        )
        d.save_svg("logo.svg")
