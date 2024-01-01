import drawsvg as dw

nord = [
    "#2e3440",
    "#3b4252",
    "#434c5e",
    "#4c566a",
    "d8dee9",
    "#e5e9f0",
    "#eceff4",
    "#8fbcbb",
    "#88c0d0",
    "#81a1c1",
    "#5e81ac",
    "#bf616a",
    "#d08770",
    "#ebc88b",
    "#a3be8c",
    "#b48ead",
]

d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 100, 200, fill="#ff0000", stroke="#00ff00"))

d.save_svg("logo.svg")
