import turtle # Tess becomes a traffic light.
import random # random

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()


# Set alex to change pensize according with tess initial state
tess.pensize(3)
tess.color("black", "darkgrey")
alex.pensize(tess.pensize())
alex.hideturtle()
alex.speed(10)
alex.color("black", "darkgrey")


def draw_housing(my_turtle):
    """ Draw a nice housing to hold the traffic lights """
    my_turtle.begin_fill()
    my_turtle.forward(80)
    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.circle(40, 180)
    my_turtle.forward(200)
    my_turtle.left(90)
    my_turtle.end_fill()


draw_housing(tess)

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3, 3, 3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 600)
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 600)
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 600)


def tess_red():
    tess.fillcolor("red")


def tess_blue():
    tess.fillcolor("blue")


def tess_green():
    tess.fillcolor("green")


def tess_yellow():
    tess.fillcolor("yellow")


def tess_pink():
    tess.fillcolor("pink")


def increase_width_pen():
    tess.clear()
    alex.clear()
    size = alex.pensize()
    if size < 20:
        tess.shapesize(3, 3, size + 1)
        alex.pensize(size + 1)
    draw_housing(alex)


def decrease_width_pen():
    tess.clear()
    alex.clear()
    size = alex.pensize()
    if size > 1:
        tess.shapesize(3, 3, size - 1)
        alex.pensize(size - 1)
    draw_housing(alex)


def increase_width_tess():
    size = tess.shapesize()[0]
    stroke = tess.shapesize()[2]
    if size < 6:
        tess.shapesize(size + 1, size + 1, stroke)


def decrease_width_tess():
    size = tess.shapesize()[0]
    stroke = tess.shapesize()[2]
    if size > 1:
        tess.shapesize(size - 1, size - 1, stroke)


# global colors
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']


def background_changer():
    global col
    ind = random.randint(0, 7)
    wn.bgcolor(col[ind])
    wn.ontimer(background_changer, 50)


def tess_changer():
    global col
    ind = random.randint(0, 7)
    tess.fillcolor(col[ind])
    wn.ontimer(tess_changer, 50)


def traffic_light_changer():
    global col
    ind = random.randint(0, 7)
    alex.color("black", col[ind])
    draw_housing(alex)


# Bind the event handler to the space key.
# wn.onkey(advance_state_machine, 'space')
wn.ontimer(advance_state_machine, 600)
wn.onkey(background_changer, 'w')
wn.onkey(tess_changer, 's')
wn.onkey(traffic_light_changer, 't')
wn.onkeypress(tess_red, 'r')
wn.onkeypress(tess_blue, 'b')
wn.onkeypress(tess_green, 'g')
wn.onkeypress(tess_yellow, 'y')
wn.onkeypress(tess_pink, 'p')
wn.onkey(increase_width_pen, "+")
wn.onkey(decrease_width_pen, "-")
wn.onkey(increase_width_tess, "Up")
wn.onkey(decrease_width_tess, "Down")
wn.listen() # Listen for events
wn.mainloop()