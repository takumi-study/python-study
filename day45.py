sx = cx + r * 0.9 * math.sin(sec_angle)
sy = cy - r * 0.9 * math.cos(sec_angle)
canvas.create_line(cx, cy, sx, sy, fill="red")
