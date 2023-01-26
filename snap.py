import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL


root = Tk()
root.title('Снэп')
c = Canvas(root, width=400, height=400)


shape = None
previous_color = ''
current_color = ''
player1_score = 0
player2_score = 0

shapes = []


def create_shapes():
    shapes = []

    circle_id = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
    shapes.append(circle_id)
    circle_id = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
    shapes.append(circle_id)
    circle_id = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
    shapes.append(circle_id)
    circle_id = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(circle_id)

    rectangle_id = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
    shapes.append(rectangle_id)
    rectangle_id = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
    shapes.append(rectangle_id)
    rectangle_id = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
    shapes.append(rectangle_id)
    rectangle_id = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(rectangle_id)

    square_id = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
    shapes.append(square_id)
    square_id = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
    shapes.append(square_id)
    square_id = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
    shapes.append(square_id)
    square_id = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
    shapes.append(square_id)

    c.pack()

    random.shuffle(shapes)

    return shapes


def init_game_settings():
    global shape
    global previous_color
    global current_color
    global player1_score
    global player2_score

    shape = None
    previous_color = ''
    current_color = ''
    player1_score = 0
    player2_score = 0


def start_game():
    global shapes

    c.delete("all")
    init_game_settings()
    shapes = create_shapes()
    next_shape()


def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color = current_color

    c.delete(shape)

    if len(shapes) > 0:
        shape = shapes.pop()
        c.itemconfigure(shape, state=NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        # c.unbind('q')
        # c.unbind('p')

        if player1_score > player2_score:
            c.create_text(200, 200, text='Победил игрок 1')
        elif player2_score > player1_score:
            c.create_text(200, 200, text='Победил игрок 2')
        else:
            c.create_text(200, 200, text='Ничья')
        c.pack()

        root.after(3000, start_game)


def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True

    if valid:
        if event.char == 'q':
            player1_score = player1_score + 1
        else:
            player2_score = player2_score + 1

        shape = c.create_text(200, 200, text='СНЭП! Вы получаете 1 очко!')
    else:
        if event.char == 'q':
            player1_score = player1_score - 1
        else:
            player2_score = player2_score - 1

        shape = c.create_text(200, 200, text='МИМО! Вы теряете 1 очко!')

    c.pack()
    root.update_idletasks()
    time.sleep(1)


root.after(3000, start_game)


c.bind('q', snap)
c.bind('p', snap)
c.focus_set()

root.mainloop()



