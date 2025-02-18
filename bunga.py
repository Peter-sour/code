import turtle

# Fungsi untuk menggambar kelopak
def draw_flower(petals, radius):
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(10)

    # Gambar kelopak
    for _ in range(petals):
        pen.circle(radius, 60)  # Lengkung pertama
        pen.left(120)
        pen.circle(radius, 60)  # Lengkung kedua
        pen.left(120)
    
    # Selesaikan
    pen.hideturtle()
    screen.mainloop()

# Parameter bunga
jumlah_kelopak = 8
radius_bunga = 100

# Gambar bunga
draw_flower(jumlah_kelopak, radius_bunga)
