import turtle 


def draw_square(t, sz):
    """Make turtle t draw a square of sz.""" 
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen() # Set up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Alex meets a function")
alex = turtle.Turtle() 	# Create alex
alex.color("#ff6699")
alex.pensize(2)
for j in range(1,6,1):
    draw_square(alex, 20*j)  # Call the function to draw the square
    alex.penup()
    alex.setx(-10*j)
    alex.sety(-10*j)
    alex.pendown()
wn.mainloop()