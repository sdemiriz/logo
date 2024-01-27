import centered_logo as center
import repeated_logo as repeat
import yaml

with open("centered_logo.yaml", "r") as file:
    image_config = yaml.safe_load(file)

with open("logo.yaml", "r") as file:
    logo_config = yaml.safe_load(file)

for logo in image_config:
    if image_config[logo]["type"] == "centered":
        center.CenteredLogo(
            canvas_dimensions=image_config[logo]["dimensions"],
            background_color=image_config[logo]["background_color"],
            major_curve_color=image_config[logo]["major_curve_color"],
            minor_curve_color=image_config[logo]["minor_curve_color"],
            logo_scale=image_config[logo]["logo_scale"],
            filename=image_config[logo]["filename"],
            debug=image_config[logo]["debug"],
            curve_height=logo_config["curve_height"],
            curve_width=logo_config["curve_width"],
            curve_thickness=logo_config["curve_thickness"],
            major_curve_separation=logo_config["major_curve_separation"],
        )

    if image_config[logo]["type"] == "repeated":
        repeat.RepeatedLogo(
            canvas_dimensions=image_config[logo]["dimensions"],
            background_color=image_config[logo]["background_color"],
            major_curve_color=image_config[logo]["major_curve_color"],
            minor_curve_color=image_config[logo]["minor_curve_color"],
            logo_scale=image_config[logo]["logo_scale"],
            pattern_repeat=image_config[logo]["pattern_repeat"],
            filename=image_config[logo]["filename"],
            debug=image_config[logo]["debug"],
            curve_height=logo_config["curve_height"],
            curve_width=logo_config["curve_width"],
            curve_thickness=logo_config["curve_thickness"],
            major_curve_separation=logo_config["major_curve_separation"],
        )
