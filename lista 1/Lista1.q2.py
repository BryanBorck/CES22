import turtle 


def draw_poly(t, n, sz):
    """Make turtle t draw a square of sz.""" 
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen() # Set up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Alex meets a function")
tess = turtle.Turtle() 	# Create alex
tess.color("#ff6699")
tess.pensize(2)
draw_poly(tess, 8, 50)  # Call the function to draw the polygon
wn.mainloop()