def decorate(screen, pen, tips):
    pen.penup()

    def flower(x, y):
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8)]:
            pen.goto(x + dx, y + dy)
            pen.dot(11, "#ff70b8")
        pen.goto(x, y)
        pen.dot(8, "#ffe16a")
        screen.update()

    for x, y in tips:
        flower(x, y)

    screen.onclick(flower)
