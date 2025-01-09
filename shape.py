import turtle

screen = turtle.Screen()


sides = int(input("How many sides does your shape have : "))
def new_func(screen, sides):
    for i in range(sides):
      turtle.forward(90)
      turtle.left(360 / sides)
  
    turtle.hideturtle()
    screen.mainloop()

new_func(screen, sides)