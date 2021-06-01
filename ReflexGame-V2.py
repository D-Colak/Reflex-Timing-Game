import keyboard
import time
import turtle
my_start = (0, 0)
t = turtle.Turtle()
bob = turtle.Turtle()

t.speed(0)
bob.speed(0)

my_font = ("Arial", 30, "normal")

turtle.bgcolor('lightgreen')
bob.hideturtle()
t.hideturtle()

def intro():
    t.penup()
    t.write('Hit "F" to stop.', font=("Arial", 20, "normal"), align='center')
    t.right(90)
    t.forward(30)
    t.left(90)
    t.write("If you land on 10, you win!", font=("Arial", 20, "normal"), align='center')
    time.sleep(2)
    t.clear()
    t.pensize(10)
    t.write("Start!", font=my_font, align='center')
    time.sleep(2)
    t.clear()

def setting():
    t.hideturtle()
    t.pencolor('magenta')
    t.fillcolor('magenta')
    t.penup()
    t.goto(my_start)
    t.forward(300)
    t.seth(90)
    t.pendown()
    t.begin_fill()
    t.circle(300)
    t.end_fill()
    t.goto(0,0)
    t.seth(0)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.seth(90)
    t.pencolor('white')
    t.fillcolor('white')
    t.begin_fill()
    for x in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

def count_turtle():
    sc = turtle.Screen()
    dict_num = 0
    i = 1
    i_dict = {}
    write_xy = (0, -20)
    bob.penup()
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    while True:
        if i != 21:
            bob.write(i, font=("Arial", 50, "normal"), align='center')
            time.sleep(0.07)
            bob.clear()
            i += 1
            if keyboard.is_pressed("f"):
                i_dict[dict_num + 1] = i
                bob.goto(write_xy)
                if i == 10:
                    bob.write("You Win! Nice Job!", font=my_font, align='center')
                if i != 10:
                    bob.left(90)
                    bob.forward(20)
                    bob.right(90)
                    bob.write(f"You landed on {i}!", font=my_font, align='center')
                    bob.right(90)
                    bob.forward(40)
                    bob.left(90)
                    bob.write('Try again!', font=my_font, align='center')
                i = 0
                restart = turtle.textinput("Restart?", "Would you like to try again? Answer with Yes or No: ")
                if restart.lower() == 'yes':
                    time.sleep(3)
                    i = 0
                elif restart.lower() == 'no':
                    bob.goto(write_xy)
                    bob.clear()
                    bob.write("Thanks for playing!", font=my_font, align='center')
                    time.sleep(2)
                    break
        if i >= 21:
            i = 0

intro()
setting()
count_turtle()
turtle.bye()
