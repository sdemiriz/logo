![sdemiriz_centered_logo](img/centered_logo_2k.svg) 

# sdemiriz Personal Logo Design 
Copyright, 2024

## Terms of use:
Any use by anyone outside the owner of this repository is not allowed. Copying and modifying for your own
programmatic logo generation needs is allowed but reusing the exact product of this repository or any
image generated by it given no/minor modification to the source code is prohibited.

I reserve all rights for the use and replication of the images generated via this repository.

## The "what"
The logo is meant to invoke the appearance of both the letter "S" and a DNA-like structure with a dual helix. The
design uses flat colors of differing shades to differentiate distance, with darker color representing
the farther "strand" and the lighter color representing the "strand" facing the viewer.

The color theme used at the moment is [Nord](https://www.nordtheme.com/). More might be added over time.

## The "why"
After designing the logo by hand, I was frustrated about how I could not manage it programmatically without going
into the `.svg` file and changing values manually one at a time which, if you have worked with the format before,
is tedious and not at all engaging.

So I took it upon myself to replicate the design I came up with by hand using a programming language and some
`.svg` manipulation library. For this I chose Python and its publicly available `drawsvg` package.

## The "how"
Currently there are a number of source code files that work together to generate the "S". The breakdown is as 
follows:

- The `logo.py` script is the launch script which invokes the class from...
- The `centered_logo.py` script which uses its class to specify pairs of curves through...
- The `centered_logo.yaml` configuration file to color and size the logo using...
- The `curve.py` script that contains the logic to make the curves of the logo using its class.

The logo has an origin coordinate, from where the 
["major" and "minor" grooves](https://www.mun.ca/biology/scarr/MGA2_02-07.html), extended to Bezier curves, start
out from. Using configuration values the heights, widths, colors and even the curvatures of each part
can be adjusted. It is all parametrized and as long as the goal is to create a centered logo design on a 
flat background, all can be done through simply modifying the configuration file.

The configuration file contains a list of entries, which means that by duplicating and changing up the 
parameters specified one can produce multiple logos without interfering with previous versions, allowing 
for quick and effortless prototyping and comparisons.

## How to use:
Clone repository, `cd` to the cloned directory, create the `conda` environment or simply install the 
required dependencies manually, activate the environment if working with `conda` then run the `logo.py` script.
```
git clone https://github.com/sdemiriz/logo.git
cd logo/
conda env create -n sdemiriz-logo --file environment.yml
conda activate sdemiriz-logo
python logo.py
```

## How to modify `centered_logo.yaml`
Copy the first `logo1` segment in its entirety and paste it into the same file as a second entry under a different
name, such as `logo2` or any other name. Adjust curve parameters, colors, scaling. Adjust image dimensions and 
filename. Turn on the debug flag to visualize Bezier curve handle positions and first curves generated by 
the script (which are then duplicated for a thickness effect).

No editing on the part of the source code is required if the desire is to generate a centered logo on a plain
background.

## TODO
- Add shadows as per material design specifications where curves overlap
- Add other patters for logo use such as background repeating logos or logo on circle background
