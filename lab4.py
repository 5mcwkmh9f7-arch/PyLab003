import random
import turtle


def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)


def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # FIX: t.circle() draws the circle with its center to the left of the
    # turtle and finishes back at the starting point, so the turtle ends up at
    # the BOTTOM of the pumpkin. The stem has to start at the top instead.
    t.penup()
    t.goto(x - radius // 10, y + 2 * radius)
    t.setheading(0)
    t.pendown()

    # Drawing the stem
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()


def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    # FIX: left(120) followed by right(120) pushed the turtle up and to the
    # left on every tooth, so the mouth climbed diagonally off the face. The
    # 45 / 90 / 45 pattern ends each tooth back at heading 0, so the zigzag
    # runs level across the pumpkin.
    for _ in range(5):  # Create a simple zigzag mouth
        t.left(45)
        t.forward(width // 7)
        t.right(90)
        t.forward(width // 7)
        t.left(45)
    t.end_fill()


def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()


def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        # FIX: a star could start as low as y = 0 and is drawn downward from
        # its starting point, so stars landed on the pumpkin stems. Raising
        # the lower bound to 50 keeps every star clear of the tallest stem.
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

# Draw three jack-o-lanterns
# FIX: the pumpkins were drawn at y = -150, which left a wide empty band along
# the bottom of the window. Every y is lowered by 130 so they rest near the
# bottom. The radii are unchanged, so the proportions stay the same.
draw_pumpkin(t, -150, -280, 100)
draw_eye(t, -190, -190, 30)  # Left eye
draw_eye(t, -110, -190, 30)  # Right eye
draw_mouth(t, -190, -230, 80)  # Mouth

draw_pumpkin(t, 0, -280, 80)
draw_eye(t, -20, -200, 25)
draw_eye(t, 20, -200, 25)
draw_mouth(t, -30, -240, 60)

draw_pumpkin(t, 150, -280, 100)
draw_eye(t, 110, -190, 30)
draw_eye(t, 190, -190, 30)
draw_mouth(t, 110, -230, 80)

# Draw the night sky
draw_sky(t, 30)

# Close the turtle graphics window when clicked
turtle.exitonclick()