import turtle

# Configurar pantalla y tortuga
screen = turtle.Screen()
screen.bgcolor("lightgreen")
tortuga = turtle.Turtle()
tortuga.speed(2)
tortuga.pensize(3)
tortuga.color("darkgreen", "green")

# Caparazón (círculo)
tortuga.penup()
tortuga.goto(0, -50)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(50)
tortuga.end_fill()

# Cabeza
tortuga.penup()
tortuga.goto(0, 50)
tortuga.setheading(90)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(15)
tortuga.end_fill()

# Patas
# Delantera izquierda
tortuga.penup()
tortuga.goto(-35, 30)
tortuga.setheading(0)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(10)
tortuga.end_fill()

# Delantera derecha
tortuga.penup()
tortuga.goto(35, 30)
tortuga.setheading(0)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(10)
tortuga.end_fill()

# Trasera izquierda
tortuga.penup()
tortuga.goto(-35, -30)
tortuga.setheading(0)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(10)
tortuga.end_fill()

# Trasera derecha
tortuga.penup()
tortuga.goto(35, -30)
tortuga.setheading(0)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(10)
tortuga.end_fill()

# Cola
tortuga.penup()
tortuga.goto(0, -60)
tortuga.setheading(-90)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(5)
tortuga.end_fill()

# Final
tortuga.hideturtle()
screen.mainloop()
