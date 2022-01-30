import turtle


DIRECTION = "Right"
DIRECTION_OFFSET = {
    "Up":[0, 20],
    "Down":[0, -20],
    "Left": [-20, 0],
    "Right":[20, 0]
}

screen = turtle.Screen()

screen.screensize(500, 500)
screen.title('Snake')
screen.bgcolor('green')
screen.tracer(0)

snake = turtle.Turtle()
snake.shape('square')
snake.color('yellow')

snake.shapesize(1)
snake_body = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake.penup()

# show snake on the window
def stamp_snake(snake, snake_body):
    for section in snake_body:
        snake.goto(section)
        snake.stamp()

# start the movement of the snake
def move_snake():
    snake_body.pop(0)
    new_head = snake_body[-1].copy()
    new_head[0] += DIRECTION_OFFSET[DIRECTION][0]
    new_head[1] += DIRECTION_OFFSET[DIRECTION][1]
    snake_body.append(new_head)

    snake.clearstamps()
    snake.penup()

    for section in snake_body:
        snake.goto(section[0],section[1])
        snake.stamp()

    screen.update()

    screen.ontimer(move_snake, 500)


# create a function to change the direction to the given one
def changer_factory(direction):
    def changer():
        global DIRECTION
        if not {direction, DIRECTION} in [{"Right", "Left"}, {"Up", "Down"}]:
            DIRECTION = direction
    return changer


stamp_snake(snake, snake_body)
screen.listen()
for dir in DIRECTION_OFFSET.keys():
    screen.onkey(changer_factory(dir), dir)

move_snake()


turtle.done()
