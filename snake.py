import turtle
import time
import random
import json
from functools import partial


SCORE_FILE_NAME = "score.txt"

delay = 0.1

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")

# the width and height can be put as user's choice
wn.setup(width=1200, height=600)
wn.tracer(0)


def create_score_display(x, color):
    score_display = turtle.Turtle()
    score_display.speed(0)
    score_display.shape("square")
    score_display.color(color)
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(x, 250)

    return score_display


def create_snake(x, y, color, name):
    head = turtle.Turtle()
    head.shape("square")
    head.color(color)
    head.penup()
    head.goto(x, y)
    head.direction = "Stop"

    score_display = create_score_display(x, color)

    score_display.write("Score {} : 0 ".format(
        name), align="center", font=("candara", 24, "bold"))

    return {
        "head": head,
        "body": [],
        "initial_x": x,
        "initial_y": y,
        "color": color,
        "score_display": score_display,
        "score_counter": 0,
        "name": name,
    }


def init_food():
    food_color = random.choice(['red', 'green', 'black'])
    food_shape = random.choice(['square', 'triangle', 'circle'])

    food.speed(0)
    food.shape(food_shape)
    food.color(food_color)
    food.penup()
    food.goto(0, 100)


snakeA = create_snake(200, 0, "white", "A")
snakeB = create_snake(-200, 0, "red", "B")

snakes = [snakeA, snakeB]
food = turtle.Turtle()

high_score_display = score_display = create_score_display(0, "orange")

init_food()


def load_high_score_from_file():
    result = 0
    with open(SCORE_FILE_NAME, 'r') as file:
        raw_data = file.read()
        parsed_data = json.loads(raw_data)
        result = parsed_data['high_score']

    return result


def update_saved_high_score_in_file(high_score):
    with open(SCORE_FILE_NAME, "w") as file:
        file.write(json.dumps({"high_score": high_score}))


def display_high_score(value):
    high_score_display.clear()
    high_score_display.write("High Score : {} ".format(
        value), align="center", font=("candara", 24, "bold"))


saved_high_score = load_high_score_from_file()
high_score = saved_high_score

display_high_score(high_score)




def go_up(snake):
    if snake["head"].direction != "down":
        snake["head"].direction = "up"


def go_down(snake):
    if snake["head"].direction != "up":
        snake["head"].direction = "down"


def go_left(snake):
    if snake["head"].direction != "right":
        snake["head"].direction = "left"


def go_right(snake):
    if snake["head"].direction != "left":
        snake["head"].direction = "right"


def move_head(snake):
    if snake["head"].direction == "up":
        y = snake["head"].ycor()
        snake["head"].sety(y + 20)
    if snake["head"].direction == "down":
        y = snake["head"].ycor()
        snake["head"].sety(y - 20)
    if snake["head"].direction == "left":
        x = snake["head"].xcor()
        snake["head"].setx(x - 20)
    if snake["head"].direction == "right":
        x = snake["head"].xcor()
        snake["head"].setx(x + 20)


wn.listen()

wn.onkeypress(partial(go_up, snakeA), "Up")
wn.onkeypress(partial(go_down, snakeA), "Down")
wn.onkeypress(partial(go_left, snakeA), "Left ")
wn.onkeypress(partial(go_right, snakeA), "Right")

wn.onkeypress(partial(go_up, snakeB), "w")
wn.onkeypress(partial(go_down, snakeB), "s")
wn.onkeypress(partial(go_left, snakeB), "a ")
wn.onkeypress(partial(go_right, snakeB), "d")


def outside_window(snake):
    return snake["head"].xcor() > 590 or snake["head"].xcor() < -590 or snake["head"].ycor() > 290 or \
           snake["head"].ycor() < -290


def game_over():
    global delay, saved_high_score

    time.sleep(1)

    for snake in snakes:
        snake["head"].goto(snake["initial_x"], snake["initial_y"])
        snake["head"].direction = "Stop"

        for segment in snake["body"]:
            segment.goto(1000, 1000)

        snake["body"].clear()
        snake["score_counter"] = 0

        snake["score_display"].clear()
        snake["score_display"].write("Score {} : {} ".format(
            snake["name"], snake["score_counter"]), align="center", font=("candara", 24, "bold"))

    init_food()

    delay = 0.1

    if high_score > saved_high_score:
        saved_high_score = high_score
        update_saved_high_score_in_file(high_score)


def eat_food(snake):
    global high_score, delay, score

    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    food.goto(x, y)

    # Adding segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color(snake["color"])
    new_segment.penup()
    snake["body"].append(new_segment)

    # немного ускоряем
    delay -= 0.001
    snake["score_counter"] += 10

    if snake["score_counter"] > high_score:
        high_score = snake["score_counter"]
        display_high_score(high_score)

    snake["score_display"].clear()
    snake["score_display"].write("Score {} : {} ".format(
            snake["name"], snake["score_counter"]), align="center", font=("candara", 24, "bold"))


# Main Gameplay
while True:
    wn.update()

    for snake in snakes:
        if outside_window(snake):
            game_over()

        if snake["head"].distance(food) < 20:
            eat_food(snake)

        # Checking for head collisions with body body
        # пойти на позицию предшественника
        for index in range(len(snake["body"]) - 1, 0, -1):
            x = snake["body"][index - 1].xcor()
            y = snake["body"][index - 1].ycor()
            snake["body"][index].goto(x, y)

        # первый после головы на место головы
        if len(snake["body"]) > 0:
            x = snake["head"].xcor()
            y = snake["head"].ycor()
            snake["body"][0].goto(x, y)

        move_head(snake)

        for segment in snake["body"]:
            # врезался в себя
            if segment.distance(snake["head"]) < 20:
                game_over()

    for segment in snakeA["body"]:
        if segment.distance(snakeB["head"]) < 20:
            game_over()

    for segment in snakeB["body"]:
        if segment.distance(snakeA["head"]) < 20:
            game_over()

    if snakeA["head"].distance(snakeB["head"]) < 20:
        game_over()

    # программе ничего не делать малое время
    time.sleep(delay)


wn.mainloop()
