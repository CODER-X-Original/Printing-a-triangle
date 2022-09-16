from shutil import move
import turtle 

move = turtle.Turtle()

move.color("red") # Choose colour from here
move.pensize(5) # Size of your pen
move.shape('turtle')

def making_a_square() :
 move.right(45) # Angle 
 move.forward(300) # The size of the line
 move.right(135) # Angle 
 move.forward(400) # The size of the line 
 move.left(228) # Angle 
 move.forward(285) # The size of the line

making_a_square()