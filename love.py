import turtle

def draw_heart(t, size):
    """Menggambar bentuk hati."""
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size * 0.5, 180)  # Setengah lingkaran
    t.right(90)
    t.circle(size * 0.5, 180)  # Setengah lingkaran kedua
    t.forward(size)
    t.end_fill()

def draw_pattern():
    """Menggambar hati dengan pola unik."""
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(10)

    # Menggambar beberapa hati dalam pola melingkar
    for angle in range(0, 360, 45):  # Setiap 45 derajat
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.forward(100)
        pen.pendown()
        draw_heart(pen, size=50)

    pen.hideturtle()
    screen.mainloop()

# Panggil fungsi untuk menggambar
draw_pattern()
