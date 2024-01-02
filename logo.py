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

r = dw.Rectangle(176, 80, 200, 200)
clip = dw.ClipPath()
clip.append(r)

r2 = dw.Rectangle(176, 150, 200, 200)
clip2 = dw.ClipPath()
clip2.append(r2)

start = (400, 100)
mid1 = (150, 200)
offset1 = (0, 100)
psm1 = (start[0] + offset1[0], start[1] + offset1[1])
psm2 = (mid1[0] - offset1[0], mid1[1] - offset1[1])

mid2 = (150, 150)
end = (400, 350)
offset2 = (50, 100)
psm3 = (mid2[0] + offset2[0], mid2[1] + offset2[1])
psm4 = (end[0] - offset2[0], end[1] - offset2[1])

p = dw.Path(stroke=nord[1], fill="none", stroke_width=30, clip_path=clip)
p2 = dw.Path(stroke=nord[10], fill="none", stroke_width=30, clip_path=clip2)
p.M(*start).C(*psm1, *psm2, *mid1)
p2.M(*mid2).C(*psm3, *psm4, *end)

d.append(p2)
d.append(p)
d.append(dw.Circle(*psm1, 5, stroke="#ffffff", fill="#ffffff"))
d.append(dw.Circle(*psm2, 5, stroke="#000000", fill="#000000"))
d.append(dw.Circle(*psm3, 5, stroke="#00ff00", fill="#00ff00"))
d.append(dw.Circle(*psm4, 5, stroke="#0000ff", fill="#0000ff"))


d.save_svg("logo.svg")
