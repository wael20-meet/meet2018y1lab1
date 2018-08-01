import turtle # python needs this to use all the turtle functions
turtle.shape('classic') # changes the shape to a turtle
turtle.bgcolor('purple')
finn = turtle.clone() # creates new turtle and saves it in finn
finn.shape('classic') # changes shape of 2nd turtle to square
finn.pensize(5)
finn.right(90)
finn.forward(100)
finn.left(90)
finn.forward(30)
finn.left(90)
finn.forward(100)
charlie = turtle.clone()
charlie.shape('circle')
charlie.left(90)
charlie.forward(200)
charlie.right(90)
charlie.forward(200)
