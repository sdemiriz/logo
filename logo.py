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
d.append(dw.Rectangle(0, 0, 500, 500, fill=nord[1]))

r = dw.Rectangle(166, 80, 219, 200)
clip = dw.ClipPath()
clip.append(r)

r2 = dw.Rectangle(166, 150, 219, 200)
clip2 = dw.ClipPath()
clip2.append(r2)

start = (400, 100)
mid = (150, 200)
offset = (0, 100)
psm_1 = (start[0] + offset[0], start[1] + offset[1])
psm_2 = (mid[0] - offset[0], mid[1] - offset[1])

mid2 = (150, 150)
psm_3 = (150, 200)
psm_4 = (350, 200)
end = (400, 350)

p = dw.Path(stroke=nord[10], fill="none", stroke_width=30, clip_path=clip)
p2 = dw.Path(stroke=nord[8], fill="none", stroke_width=30, clip_path=clip2)
p.M(*start).C(*psm_1, *psm_2, *mid)
p2.M(*mid2).C(*psm_3, *psm_4, *end)

d.append(p)
d.append(p2)
d.append(dw.Circle(*psm_1, 5, stroke="#ffffff", fill="#ffffff"))
d.append(dw.Circle(*psm_2, 5, stroke="#000000", fill="#000000"))
d.append(dw.Circle(*psm_3, 5, stroke="#00ff00", fill="#00ff00"))
d.append(dw.Circle(*psm_4, 5, stroke="#0000ff", fill="#0000ff"))


d.save_svg("logo.svg")
