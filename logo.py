import drawsvg as dw

d = dw.Drawing(500, 500, id_prefix="pic")
d.append(dw.Rectangle(0, 0, 100, 200, fill="#ff0000", stroke="#00ff00"))

d.save_svg("logo.svg")
