import turtle
import time
import random
import json


SCORE_FILE_NAME = "score.txt"

delay = 0.1
score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")

# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)


# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)


def load_high_score_from_file():
    result = 0
    with open(SCORE_FILE_NAME, 'r') as file:
        raw_data = file.read()
        parsed_data = json.loads(raw_data)
        result = parsed_data['high_score']

    return result


def update_saved_high_score_in_file(high_score):
    with open(SCORE_FILE_NAME, "w") as file:
        file.write(json.dumps({"high_score": high_score, "test_data": "test"}))


saved_high_score = load_high_score_from_file()
high_score = saved_high_score

pen.write("Score : 0 High Score : {} ".format(
        high_score), align="center", font=("candara", 24, "bold"))


# assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move_head():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left ")
wn.onkeypress(go_right, "Right")


segments = []


def outside_window():
    return head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290


def game_over():
    global colors, shapes, delay, score, saved_high_score

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"

    colors = random.choice(['red', 'blue', 'green'])
    shapes = random.choice(['square', 'circle'])

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()
    score = 0
    delay = 0.1
    pen.clear()
    pen.write("Score : {} High Score : {} ".format(
        score, high_score), align="center", font=("candara", 24, "bold"))

    if high_score > saved_high_score:
        saved_high_score = high_score
        update_saved_high_score_in_file(high_score)


def eat_food():
    global high_score, delay, score

    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    food.goto(x, y)

    # Adding segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("orange")  # tail colour
    new_segment.penup()
    segments.append(new_segment)

    # немного ускоряем
    delay -= 0.001
    score += 10

    if score > high_score:
        high_score = score

    pen.clear()
    pen.write("Score : {} High Score : {} ".format(
        score, high_score), align="center", font=("candara", 24, "bold"))


# Main Gameplay
while True:
    wn.update()

    if outside_window():
        game_over()

    if head.distance(food) < 20:
        eat_food()

    # Checking for head collisions with body segments
    # пойти на позицию предшественника
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # первый после головы на место головы
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move_head()

    for segment in segments:
        # врезался в себя
        if segment.distance(head) < 20:
            game_over()

    # программе ничего не делать малое время
    time.sleep(delay)


wn.mainloop()
