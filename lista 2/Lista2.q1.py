import turtle 


def draw_square(t, sz):
    """Make turtle t draw a square of sz.""" 
    for i in range(4):
        t.forward(sz)
        t.left(90)


turtle.setup(800,800)
wn = turtle.Screen() # Set up the window and its attributes 
wn.bgcolor("white") 
wn.title("Alex meets a function")
alex = turtle.Turtle() 	# Create alex
alex.color("black")
alex.speed(2)
alex.pensize(2)

def drawing():
     j = 0
     while True:
          wn.listen()
          wn.onkey(alex_red, 'r')
          wn.onkey(alex_blue, 'b')
          wn.onkey(alex_green, 'g')
          wn.onkey(increase_width_pen, "+")
          wn.onkey(decrease_width_pen, "-")
          j += 1
          draw_square(alex, 20*j)  # Call the function to draw the square
          alex.penup()
          alex.setx(-10*j)
          alex.sety(-10*j)
          alex.pendown()


def alex_red():
    alex.color("red")


def alex_blue():
    alex.color("blue")


def alex_green():
    alex.color("green")


def increase_width_pen():
    size = alex.pensize()
    if size < 20:
        alex.pensize(size + 1)


def decrease_width_pen():
    size = alex.pensize()
    if size > 1:
        alex.pensize(size - 1)


drawing()