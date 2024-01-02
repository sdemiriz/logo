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

start = (400, 100)
psm_1 = (350, 150)
psm_2 = (150, 100)
mid = (150, 200)
p = dw.Path(stroke="#ff4444", fill="none", stroke_width=30)
p.M(*start).C(*psm_1, *psm_2, *mid)
d.append(p)
d.append(dw.Circle(*psm_1, 5, stroke="#ffffff", fill="#ffffff"))
d.append(dw.Circle(*psm_2, 5, stroke="#000000", fill="#000000"))

psm_3 = (150, 250)
psm_4 = (350, 250)
end = (400, 400)
p2 = dw.Path(stroke="#ff6666", fill="none", stroke_width=30)
p2.M(*mid).C(*psm_3, *psm_4, *end)
d.append(p2)

d.append(dw.Circle(*psm_3, 5, stroke="#00ff00", fill="#00ff00"))
d.append(dw.Circle(*psm_4, 5, stroke="#0000ff", fill="#0000ff"))


d.save_svg("logo.svg")
