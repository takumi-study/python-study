    # 文字盤（1〜12）
    for i in range(12):
        angle = math.radians(i * 30)

        x = cx + r * 0.8 * math.sin(angle)
        y = cy - r * 0.8 * math.cos(angle)

        num = i if i != 0 else 12
        canvas.create_text(x, y, text=str(num), font=("Arial", 12))