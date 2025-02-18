import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Membuat objek turtle
t = turtle.Turtle()
t.speed(10)

# Fungsi untuk menggambar gunung
def draw_mountain(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(150)
        t.left(120)
    t.end_fill()

# Fungsi untuk menggambar matahari
def draw_sun(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi untuk menggambar awan
def draw_cloud(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(6):
        t.circle(size, 180)
        t.right(60)
    t.end_fill()

# Fungsi untuk menggambar jalan sawah
def draw_road():
    t.penup()
    t.goto(-300, -100)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.goto(300, -100)
    t.goto(300, -300)
    t.goto(-300, -300)
    t.goto(-300, -100)
    t.end_fill()

# Fungsi untuk menggambar burung
def draw_bird(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(45)
    for _ in range(2):
        t.circle(20, 90)
        t.right(180)

# Fungsi untuk menggambar pesawat
def draw_airplane(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10, 180)
    t.goto(x + 40, y)
    t.goto(x + 20, y + 20)
    t.goto(x - 20, y + 20)
    t.goto(x, y)
    t.end_fill()

# Gambar gunung
draw_mountain(-400, -100, "gray")
draw_mountain(0, -100, "brown")
draw_mountain(400, -100, "dark gray")

# Gambar matahari
draw_sun(0, 200, 50)

# Gambar awan
draw_cloud(-300, 100, 30)
draw_cloud(200, 150, 20)

# Gambar sawah
draw_road()

# Gambar burung
draw_bird(-200, 150)
draw_bird(150, 120)

# Gambar pesawat
draw_airplane(100, 180)

# Sembunyikan turtle setelah menggambar
t.hideturtle()

# Menjaga layar tetap terbuka
turtle.done()

