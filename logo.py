import centered_logo as center
import repeated_logo as repeat
import yaml

with open("centered_logo.yaml", "r") as file:
    config = yaml.safe_load(file)

for logo in config:
    if config[logo]["type"] == "centered":
        center.CenteredLogo(
            canvas_dimensions=config[logo]["dimensions"],
            background_color=config[logo]["background_color"],
            major_curve_color=config[logo]["major_curve_color"],
            minor_curve_color=config[logo]["minor_curve_color"],
            curve_height=config[logo]["curve_height"],
            curve_width=config[logo]["curve_width"],
            curve_thickness=config[logo]["curve_thickness"],
            major_curve_separation=config[logo]["major_curve_separation"],
            logo_scale=config[logo]["logo_scale"],
            filename=config[logo]["filename"],
            debug=config[logo]["debug"],
        )

    if config[logo]["type"] == "repeated":
        repeat.RepeatedLogo(
            canvas_dimensions=config[logo]["dimensions"],
            background_color=config[logo]["background_color"],
            major_curve_color=config[logo]["major_curve_color"],
            minor_curve_color=config[logo]["minor_curve_color"],
            curve_height=config[logo]["curve_height"],
            curve_width=config[logo]["curve_width"],
            curve_thickness=config[logo]["curve_thickness"],
            major_curve_separation=config[logo]["major_curve_separation"],
            logo_scale=config[logo]["logo_scale"],
            filename=config[logo]["filename"],
            debug=config[logo]["debug"],
        )
