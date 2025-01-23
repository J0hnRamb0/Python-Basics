import turtle

screen = turtle.Screen()
shape = input("Enter the shape you want to draw: \nSelect 1 for Circle \nSelect 2 for Square \nSelect 3 for Triangle \nSelect 4 for Rectangle \nEnter your choice : ")

if shape == '1':
    turtle.circle(100)

elif shape == '2':
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

elif shape == '3':
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

elif shape == '4':
    for i in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

else:
    print("Invalid choice")


turtle.hideturtle()

screen.mainloop()