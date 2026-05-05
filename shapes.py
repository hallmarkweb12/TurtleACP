import turtle
turtle.title("Drawing Shapes")
turtle.Screen().bgcolor("red")
#Equilateral Triangle
turtle.fillcolor("black")
turtle.begin_fill()
for i in range(3):
    turtle.forward(120)
    turtle.left(120)
turtle.end_fill()    

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

#Hexagon  
turtle.fillcolor("yellow")      
turtle.begin_fill()
for i in range(6):
    turtle.forward(60)   
    turtle.left(60) 
turtle.end_fill()    

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()

#Rectangle
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()
turtle.done()    