# Ready
import turtle as t
import random as r

# -----------------------------
# Window
# -----------------------------
w = t.Screen()
w.setup(800, 600)
w.bgcolor("white")
w.title("贪吃蛇666 Snake V2")
w.tracer(0)
w.listen()

FONT = ("msyh.ttc", 18, "normal")
BIGFONT = ("msyh.ttc", 26, "bold")

# -----------------------------
# Snake body
# -----------------------------
def body():
    b = t.Turtle()
    b.shape("circle")
    b.color("green")
    b.penup()
    b.speed(0)
    return b

# -----------------------------
# Pens
# -----------------------------
score_pen = t.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-380,260)

popup_pen = t.Turtle()
popup_pen.hideturtle()
popup_pen.penup()

game_pen = t.Turtle()
game_pen.hideturtle()
game_pen.penup()

# -----------------------------
# Globals
# -----------------------------
score = 0

snake = []

food = t.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)

foodx = 0
foody = 0

popup_alive = False
popup_frame = 0
popup_x = 0
popup_y = 0

running = True

# -----------------------------
# Score
# -----------------------------
def draw_score():
    score_pen.clear()
    score_pen.write(
        f"Score : {score}",
        font=FONT
    )

# -----------------------------
# Popup +1
# -----------------------------
def popup():

    global popup_alive,popup_frame,popup_x,popup_y

    popup_alive=True
    popup_frame=0

    popup_x=foodx
    popup_y=foody

def update_popup():

    global popup_alive,popup_frame,popup_y

    if not popup_alive:
        return

    popup_pen.clear()

    colors=[
        "red",
        "firebrick",
        "indianred",
        "lightcoral",
        "lightpink",
        "mistyrose"
    ]

    color=colors[min(popup_frame//4,len(colors)-1)]

    popup_pen.color(color)

    popup_pen.goto(popup_x,popup_y+popup_frame*2)

    popup_pen.write(
        "+1",
        align="center",
        font=("Noto Sans CJK SC",20,"bold")
    )

    popup_frame+=1

    if popup_frame>24:
        popup_pen.clear()
        popup_alive=False

# -----------------------------
# Food
# -----------------------------
def make():

    global foodx,foody

    foodx=r.randint(-250,250)
    foody=r.randint(-250,250)

    food.goto(foodx,foody)

# -----------------------------
# Reset
# -----------------------------
def reset_game():

    global snake,score,running

    running=True

    score=0

    game_pen.clear()
    popup_pen.clear()

    for s in snake:
        s.hideturtle()

    snake=[]

    for i in range(3):
        b=body()
        b.goto(-20*i,0)
        snake.append(b)

    snake[0].setheading(0)

    draw_score()

    make()

# -----------------------------
# Move
# -----------------------------
def move():

    pos=[s.pos() for s in snake]

    snake[0].forward(10)

    for i in range(1,len(snake)):
        snake[i].goto(pos[i-1])

# -----------------------------
# Eat
# -----------------------------
def eat():

    global score

    xc=snake[0].xcor()
    yc=snake[0].ycor()

    if (xc-foodx)**2+(yc-foody)**2<400:

        score+=1

        draw_score()

        popup()

        new=body()
        new.goto(snake[-1].pos())

        snake.append(new)

        make()

        return True

    return False

# -----------------------------
# Turn
# -----------------------------
def left():
    if running:
        snake[0].left(15)

def right():
    if running:
        snake[0].right(15)

w.onkeypress(left,"Left")
w.onkeypress(right,"Right")


# -----------------------------
# Game Over
# -----------------------------
def game_over():

    global running

    running=False

    game_pen.clear()

    game_pen.goto(0,80)

    game_pen.write(
        "Game Over",
        align="center",
        font=("Noto Sans CJK SC",32,"bold")
    )

    game_pen.goto(0,20)

    game_pen.write(
        f"分数：{score}",
        align="center",
        font=("Noto Sans CJK SC",22,"normal")
    )

    game_pen.goto(0,-50)

    game_pen.write(
        "重新开始：按 R 键",
        align="center",
        font=("Noto Sans CJK SC",18,"normal")
    )

    game_pen.goto(0,-90)

    game_pen.write(
        "结束游戏：按 ESC 键",
        align="center",
        font=("Noto Sans CJK SC",18,"normal")
    )


# -----------------------------
# Restart
# -----------------------------
def restart():

    if running:
        return

    reset_game()

    game()


# -----------------------------
# Exit
# -----------------------------
def quit_game():
    w.bye()


w.onkeypress(restart,"r")
w.onkeypress(restart,"R")

w.onkeypress(quit_game,"Escape")


# -----------------------------
# Main Game
# -----------------------------
def game():

    if not running:
        return

    move()

    eat()

    update_popup()

    x=snake[0].xcor()
    y=snake[0].ycor()

    if abs(x)>390 or abs(y)>290:

        game_over()

        w.update()

        return

    w.update()

    w.ontimer(game,100)


# -----------------------------
# Start
# -----------------------------
reset_game()

game()

w.mainloop()
