import drawsvg as dw
import curve as c
import nord as n


class CenteredLogo:
    def __init__(self, canvas_dimensions):
        self.canvas_dimensions = canvas_dimensions
        self.minor_curve_multiplier = 12
        self.major_curve_multiplier = 22

        d = dw.Drawing(
            self.canvas_dimensions[0], self.canvas_dimensions[1], id_prefix="pic"
        )
        d.append(
            dw.Rectangle(
                0,
                0,
                self.canvas_dimensions[0],
                self.canvas_dimensions[1],
                fill=n.nord[1],
            )
        )

        overall_scaling = 1.5

        curve_height = int(10 * overall_scaling)
        curve_width = int(300 * overall_scaling)
        thickness = int(42 * overall_scaling)

        copy_offset_major = int(-84 * overall_scaling)

        curve_left = (self.canvas_dimensions[0] - curve_width) / 2
        curve_top = (
            self.canvas_dimensions[1]
            - (self.major_curve_multiplier * curve_height)
            - (copy_offset_major / 2)
        ) / 2

        start_major = (curve_left, curve_top)
        size = (curve_width, self.major_curve_multiplier * curve_height)
        end_major = (start_major[0] + size[0], start_major[1] + size[1])
        offset = (0 * overall_scaling, -100 * overall_scaling)

        c.Curve(
            drawing=d,
            start=start_major,
            end=end_major,
            thickness=thickness,
            offset=offset,
            color=n.nord[10],
            debug=False,
        )

        c.Curve(
            drawing=d,
            start=(start_major[0], start_major[1] + copy_offset_major),
            end=(end_major[0], end_major[1] + copy_offset_major),
            thickness=thickness,
            offset=offset,
            color=n.nord[10],
            debug=False,
        )

        start_minor = (curve_left, curve_top)
        size = (curve_width, -self.minor_curve_multiplier * curve_height)
        end_minor = (start_minor[0] + size[0], start_minor[1] + size[1])
        copy_offset_minor = copy_offset_major + (
            (self.major_curve_multiplier + self.minor_curve_multiplier) * curve_height
        )
        offset = (0, offset[1] * -1)

        c.Curve(
            drawing=d,
            start=start_minor,
            end=end_minor,
            thickness=thickness,
            offset=offset,
            color=n.nord[9],
            debug=False,
        )

        c.Curve(
            drawing=d,
            start=(start_minor[0], start_minor[1] + copy_offset_minor),
            end=(end_minor[0], end_minor[1] + copy_offset_minor),
            thickness=thickness,
            offset=offset,
            color=n.nord[9],
            debug=False,
        )
        d.save_svg("logo.svg")
