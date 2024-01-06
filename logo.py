import centered_logo as center
import yaml

with open("centered_logo.yaml", "r") as file:
    config = yaml.safe_load(file)

for logo in config:
    if config[logo]["type"] == "centered":
        center.CenteredLogo(canvas_dimensions=config[logo]["dimensions"])
