import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Display")

# Create a turtle for the fireworks
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)
firework.width(1)

# List of colors for the fireworks
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]

# Create a turtle for the moon
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
moon.color("gray")

def draw_moon():
    moon.penup()
    moon.goto(-200, 200)
    moon.pendown()
    moon.begin_fill()
    moon.circle(50)
    moon.end_fill()

# Create a turtle for the stars
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.color("white")

# Function to draw the stars
def draw_stars():
    stars.penup()
    for _ in range(50):  # Number of stars
        x = random.randint(-400, 400)
        y = random.randint(100, 400)  # Y-coordinates above 100
        stars.goto(x, y)
        stars.dot(random.randint(2, 5))  # Random size between 2 and 5 pixels

# Function to draw a firework explosion
def draw_firework(x, y, size, color):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.color(color)
    for _ in range(36):
        firework.forward(size)
        firework.backward(size)
        firework.right(10)

# Function to simulate a firework shoot
def shoot_firework():
    # Random starting position at the bottom of the screen
    start_x = random.randint(-300, 300)
    start_y = -300  # Start at the bottom of the screen
    color = random.choice(colors)
    size = random.randint(20, 150)

    # Random angle for the firework (between 60 and 120 degrees)
    angle = random.randint(60, 120)
    
    # Draw the line upwards from start_y
    firework.penup()
    firework.goto(start_x, start_y)
    firework.pendown()
    firework.setheading(angle)

    # Simulate upwards movement with small steps and slight horizontal deviation
    for _ in range(60):
        firework.forward(5)  # Small forward step
        firework.right(random.randint(-2, 2))  # Slight random horizontal deviation

    # Draw the explosion at the top of the line
    draw_firework(firework.xcor(), firework.ycor(), size, color)

def write_name():
    name = turtle.Turtle()
    name.hideturtle()
    name.speed(0)
    name.color("white")
    name.penup()
    name.goto(350, -250)
    name.pendown()
    name.write("J.Y.", align="right", font=("Arial", 18, "normal"))

# Draw the moon, stars, and background
draw_moon()
draw_stars()

# Write name
write_name()

# Simulate multiple fireworks going off
for _ in range(12):  # Number of fireworks
    shoot_firework()

# Keep the window open
screen.mainloop()
