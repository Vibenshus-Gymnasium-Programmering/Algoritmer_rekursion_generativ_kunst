import turtle
import random

SCREEN_WIDTH = 800

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_WIDTH)
screen.colormode(255)


def draw_square(
    turtle, lower_left_x, lower_left_y, width, fill_color, pen_color=(255, 255, 255)
):
    turtle.fillcolor(fill_color)
    turtle.pencolor(pen_color)
    turtle.penup()
    turtle.goto(lower_left_x, lower_left_y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def split_or_fill(turtle, x, y, width, level, max_level):
    if level <= max_level:
        # Base case - filling
        # The chance to fill grows evenly with the level
        # At level 0 it must split
        # At the last level it must fill
        fill = random.randint(0, 100) < level * 100 / max_level #or level == max_level 
        if fill:
            # r = random.randint(0, 255)
            r = random.randint(0, 100)
            g = random.randint(0, 100)
            b = random.randint(0, 100)
            # b = 255
            fill_color = (r, g, b)
            draw_square(turtle, x, y, width, fill_color)
        # Recursive case - splitting
        else:  # split
            # number_of_rows_and_columns = 2
            number_of_rows_and_columns = random.randint(2,3)
            for row in range(number_of_rows_and_columns):
                for col in range(number_of_rows_and_columns):
                    split_or_fill(turtle, x + col * width / number_of_rows_and_columns, y + row * width / number_of_rows_and_columns, width / number_of_rows_and_columns, level + 1, max_level)


# Setup screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_WIDTH)
screen.colormode(255)

# Setup turtle
turtle = turtle.Turtle()
turtle.speed(0)
turtle.hideturtle()

# Using seed to be able to recreate "random" images
# random.seed(42)
# Run recursive function
split_or_fill(turtle, -SCREEN_WIDTH / 2, -SCREEN_WIDTH / 2, SCREEN_WIDTH, 0, 5)

# Keep screen open
screen.mainloop()
