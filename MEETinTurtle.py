
import turtle

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...
turtle.penup() 	#Brings the pen up, so
				#nothing will be drawn
turtle.pendown()	#Puts the pen down, so we
				#are ready to draw!
turtle.goto(x,y) #Go to the position “x"&"y", 
#but write in numbers 
#instead


# ...and end it before the next line.
turtle.mainloop()

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100) 


