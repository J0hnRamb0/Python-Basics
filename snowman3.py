import turtle 

turtle.speed(-10)

turtle.colormode(255)

screen = turtle.Screen()
# Bottom of the snowman
turtle.begin_fill()
for i in range(36):
    turtle.color(211, 211, 211)
    turtle.fillcolor((242,243,244)) 
    turtle.forward(18)
    turtle.right(10)
turtle.end_fill()

# Middle of the snowman
turtle.begin_fill()
for i in range(36):
    turtle.color(211, 211, 211)
    turtle.fillcolor((242,243,244))
    turtle.forward(12)
    turtle.left(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 138)
turtle.pendown()
# Head of the snowman
for i in range(36):
    turtle.forward(9)
    turtle.left(10)
# Eyes of the snowman
turtle.begin_fill()
turtle.color(0, 0, 0)
turtle.fillcolor(( 0, 0, 0))
turtle.penup()
turtle.goto(-15, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.goto(24, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.penup()
turtle.goto(-13, 177)
turtle.pendown()

turtle.setheading(270)

# snowman smile
for i in range(13): 
    turtle.forward(5)
    turtle.left(15)

turtle.penup()
turtle.goto(-45, 115)
turtle.pendown()



# rightarm


turtle.penup()
turtle.goto(-57, 94)
turtle.pendown()
turtle.setheading(160)
turtle.forward(80)

# top right arm

turtle.penup()
turtle.goto(-130,122)
turtle.pendown()
turtle.setheading(100)
turtle.forward(80)

# lift arm 

turtle.penup()
turtle.goto(72,84)
turtle.pendown()
turtle.setheading(-340)
turtle.forward(80)

# upper# left arm 

turtle.penup()
turtle.goto(145,110)
turtle.pendown()
turtle.setheading(-280)
turtle.forward(80)

# glove left
turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,36,0))
turtle.goto(159,187)
turtle.pendown()
turtle.setheading(-365)
turtle.forward(15)
turtle.goto(173,214)
turtle.setheading(-195)
turtle.forward(25)
turtle.setheading(-90)
turtle.forward(23)
turtle.setheading(-195)
turtle.forward(7)
turtle.setheading(-90)
turtle.forward(15)
turtle.setheading(-10)
turtle.forward(10)
turtle.setheading(10)
turtle.forward(9)
turtle.end_fill()
turtle.penup()

# glove right

turtle.begin_fill()

turtle.goto(-142,198)
turtle.pendown()
turtle.setheading(-365)
turtle.fillcolor((255,36,0))
turtle.forward(13)
turtle.setheading(-280)
turtle.forward(19)
turtle.setheading(-189)
turtle.forward(14)
turtle.setheading(-280)
turtle.forward(28)
turtle.setheading(-180)
turtle.forward(28)
turtle.setheading(-80)
turtle.forward(50)
turtle.setheading(1)
turtle.forward(25)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 0)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -150)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(-13, 177)
turtle.pendown()
turtle.end_fill()

#bottom of hat 
turtle.penup()
turtle.goto(-60, 233)
turtle.begin_fill()
turtle.pendown()
turtle.forward(130) 
turtle.left(87) 
turtle.forward(15) 
turtle.left(90)
turtle.forward(130) 
turtle.end_fill()

#top of hat
turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(-25, 251)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50) 
turtle.right(40)
turtle.setheading(0)
turtle.forward(55) 
turtle.right(40)
turtle.setheading(-90)
turtle.forward(50) 
turtle.right(40)
turtle.end_fill()


#ground
turtle.penup()
turtle.color(211, 211, 211)
turtle.goto(-375, -160)
turtle.begin_fill()
turtle.setheading(0)
turtle.pendown()
turtle.forward(300) 
turtle.right(60)

turtle.penup()
turtle.color(255,255,255)
turtle.goto(-375, -160)
turtle.begin_fill()
turtle.setheading(0)
turtle.pendown()
turtle.forward(300) 
turtle.right(60)

turtle.penup()
turtle.color(211, 211, 211)
turtle.goto(-375, -160)
turtle.begin_fill()
turtle.setheading(0)
turtle.pendown()
turtle.forward(300) 
turtle.right(60)

turtle.penup()
turtle.color(255,255,255)
turtle.goto(-375, -160)
turtle.begin_fill()
turtle.setheading(0)
turtle.pendown()
turtle.forward(300) 
turtle.right(60)



turtle.penup()
turtle.goto(0, 138)
turtle.pendown()
# Head of the snowman
for i in range(36):
    turtle.forward(9)
    turtle.left(10)
# Eyes of the snowman
turtle.begin_fill()
turtle.color(255,255,255)
turtle.fillcolor((255,255,255))
turtle.penup()
turtle.goto(-15, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.goto(24, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.penup()
turtle.goto(-13, 177)
turtle.pendown()

turtle.setheading(270)

# snowman smile
for i in range(13): 
    turtle.forward(5)
    turtle.left(15)

turtle.penup()
turtle.goto(-45, 115)
turtle.pendown()



# rightarm


turtle.penup()
turtle.goto(-57, 94)
turtle.pendown()
turtle.setheading(160)
turtle.forward(80)

# top right arm

turtle.penup()
turtle.goto(-130,122)
turtle.pendown()
turtle.setheading(100)
turtle.forward(80)

# lift arm 

turtle.penup()
turtle.goto(72,84)
turtle.pendown()
turtle.setheading(-340)
turtle.forward(80)

# upper# left arm 

turtle.penup()
turtle.goto(145,110)
turtle.pendown()
turtle.setheading(-280)
turtle.forward(80)

# glove left
turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(159,187)
turtle.pendown()
turtle.setheading(-365)
turtle.forward(15)
turtle.goto(173,214)
turtle.setheading(-195)
turtle.forward(25)
turtle.setheading(-90)
turtle.forward(23)
turtle.setheading(-195)
turtle.forward(7)
turtle.setheading(-90)
turtle.forward(15)
turtle.setheading(-10)
turtle.forward(10)
turtle.setheading(10)
turtle.forward(9)
turtle.end_fill()
turtle.penup()

# glove right

turtle.begin_fill()

turtle.goto(-142,198)
turtle.pendown()
turtle.setheading(-365)
turtle.fillcolor((255,255,255))
turtle.forward(13)
turtle.setheading(-280)
turtle.forward(19)
turtle.setheading(-189)
turtle.forward(14)
turtle.setheading(-280)
turtle.forward(28)
turtle.setheading(-180)
turtle.forward(28)
turtle.setheading(-80)
turtle.forward(50)
turtle.setheading(1)
turtle.forward(25)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 255,255,255))
turtle.goto(10, 100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 255,255,255))
turtle.goto(10, 50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(10, 0)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(10, -50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(10, -100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(10, -150)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,255,255))
turtle.goto(-13, 177)
turtle.pendown()
turtle.end_fill()

#bottom of hat 
turtle.penup()
turtle.goto(-60, 233)
turtle.begin_fill()
turtle.pendown()
turtle.forward(130) 
turtle.left(87) 
turtle.forward(15) 
turtle.left(90)
turtle.forward(130) 
turtle.end_fill()

#top of hat
turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 255,255,255))
turtle.goto(-25, 251)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50) 
turtle.right(40)
turtle.setheading(0)
turtle.forward(55) 
turtle.right(40)
turtle.setheading(-90)
turtle.forward(50) 
turtle.right(40)
turtle.end_fill()


turtle.penup()
turtle.goto(0, 138)
turtle.pendown()
# Head of the snowman
for i in range(36):
    turtle.forward(9)
    turtle.left(10)
# Eyes of the snowman
turtle.begin_fill()
turtle.color(0, 0, 0)
turtle.fillcolor(( 0, 0, 0))
turtle.penup()
turtle.goto(-15, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.goto(24, 200)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.penup()
turtle.goto(-13, 177)
turtle.pendown()

turtle.setheading(270)

# snowman smile
for i in range(13): 
    turtle.forward(5)
    turtle.left(15)

turtle.penup()
turtle.goto(-45, 115)
turtle.pendown()



# rightarm


turtle.penup()
turtle.goto(-57, 94)
turtle.pendown()
turtle.setheading(160)
turtle.forward(80)

# top right arm

turtle.penup()
turtle.goto(-130,122)
turtle.pendown()
turtle.setheading(100)
turtle.forward(80)

# lift arm 

turtle.penup()
turtle.goto(72,84)
turtle.pendown()
turtle.setheading(-340)
turtle.forward(80)

# upper# left arm 

turtle.penup()
turtle.goto(145,110)
turtle.pendown()
turtle.setheading(-280)
turtle.forward(80)

# glove left
turtle.begin_fill()
turtle.penup()
turtle.fillcolor((255,36,0))
turtle.goto(159,187)
turtle.pendown()
turtle.setheading(-365)
turtle.forward(15)
turtle.goto(173,214)
turtle.setheading(-195)
turtle.forward(25)
turtle.setheading(-90)
turtle.forward(23)
turtle.setheading(-195)
turtle.forward(7)
turtle.setheading(-90)
turtle.forward(15)
turtle.setheading(-10)
turtle.forward(10)
turtle.setheading(10)
turtle.forward(9)
turtle.end_fill()
turtle.penup()

# glove right

turtle.begin_fill()

turtle.goto(-142,198)
turtle.pendown()
turtle.setheading(-365)
turtle.fillcolor((255,36,0))
turtle.forward(13)
turtle.setheading(-280)
turtle.forward(19)
turtle.setheading(-189)
turtle.forward(14)
turtle.setheading(-280)
turtle.forward(28)
turtle.setheading(-180)
turtle.forward(28)
turtle.setheading(-80)
turtle.forward(50)
turtle.setheading(1)
turtle.forward(25)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, 0)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -50)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -100)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(10, -150)
turtle.pendown()
turtle.circle(4)
turtle.end_fill()


turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(-13, 177)
turtle.pendown()
turtle.end_fill()

#bottom of hat 
turtle.penup()
turtle.goto(-60, 233)
turtle.begin_fill()
turtle.pendown()
turtle.forward(130) 
turtle.left(87) 
turtle.forward(15) 
turtle.left(90)
turtle.forward(130) 
turtle.end_fill()

#top of hat
turtle.begin_fill()
turtle.penup()
turtle.fillcolor(( 0, 0, 0))
turtle.goto(-25, 251)
turtle.pendown()
turtle.setheading(90)
turtle.forward(50) 
turtle.right(40)
turtle.setheading(0)
turtle.forward(55) 
turtle.right(40)
turtle.setheading(-90)
turtle.forward(50) 
turtle.right(40)
turtle.end_fill()




turtle.penup()
turtle.hideturtle()
screen.mainloop()

#print(dir(turtle))
