import random
import turtle
import time
import os

if not os.path.exists("score.txt"):
    with open("score.txt", "w") as file:
        file.write(f"Names\tScores\n")

def score_append():
    with open("score.txt", "a") as file:
        file.write(f"{name}\t{score}\n")

def score_display():
    with open('score.txt', 'r') as file:
        for i in file:
            print(i)

        #Option to delete scores
        while True:
            choice = input("Would you like to delete scores?(Y/N):\n-").upper()
            if choice == "Y":
                remover()
            elif choice == "N":
                main_terminal()
            else:
                print("Please enter Y or N.")

def remover():
    with open('score.txt', 'r') as file:
        lines = file.readlines()

    player_to_delete = input("Enter the name of the player whose score you want to delete:\n- ").capitalize()
    found = False

    with open('score.txt', 'w') as file:
        for line in lines:
            if player_to_delete in line:
                found = True
                break

    if found:
        with open('score.txt', 'w') as file:
            for line in lines:
                if player_to_delete not in line:
                    file.write(line)
        print(f"Score for {player_to_delete} has been deleted.")
        score_display()
    else:
        print(f"No score found for {player_to_delete}.")



def pregame():
    story.hideturtle()
    t.showturtle()
    ask_question()

def start_game():
    screen.onkeypress(pregame, "k")

def main_display():
    global wrong_count, t, s, screen, story, drown, eaten, win, score

    # Create a turtle objects
    t = turtle.Turtle()
    t.speed(0)
    s = turtle.Turtle()
    s.speed(0)
    story = turtle.Turtle()
    story.speed(0)
    drown = turtle.Turtle()
    drown.speed(0)
    eaten = turtle.Turtle()
    drown.speed(0)
    win = turtle.Turtle()
    win.speed(0)
    score_display = turtle.Turtle()
    score_display.speed(0)

    # Set up the screen
    turtle.title("SwimMath")
    screen = turtle.Screen()
    screen.setup(width=683, height=483)
    screen.bgpic('Ocean.gif')
    screen.addshape('shark.gif',)
    screen.addshape('person.gif')
    screen.addshape('Story.gif')
    screen.addshape('drown.gif')
    screen.addshape('eaten.gif')
    screen.addshape('Win.gif')
    screen.listen()

    # Story
    story.penup()
    story.goto(0, 0)
    story.shape('Story.gif')

    # Win
    win.hideturtle()
    win.penup()
    win.goto(0, 0)
    win.shape('Win.gif')

    # Game overs
    drown.hideturtle()
    drown.penup()
    drown.goto(0, 0)
    drown.shape('drown.gif')

    eaten.hideturtle()
    eaten.penup()
    eaten.goto(0, 0)
    eaten.shape('eaten.gif')

    # Shark
    s.hideturtle()
    s.penup()
    s.shape('shark.gif')
    s.goto(-200, -255)
    s.setheading(90)
    s.showturtle()
    s.speed(1)

    # Person
    t.hideturtle()
    t.shape('person.gif')
    t.turtlesize(3)
    t.penup()
    t.setheading(60)
    t.goto(-300, -200)  # Move turtle to the bottom left of the screen
    t.speed(2)

    # Initialize the variables needed
    score = 0
    wrong_count = 0
def ask_name():
    global name

    print("""<<<<<<< Welcome to SwimMath >>>>>>>
     ||  ENTER PLAYER NAME  ||""")
    name = str(input("-"))
    print(f"====> Hi {name}, please press [K]\n\n")
    return name

def question():

    # Random integer
    rndm1 = random.randint(1, 10)
    rndm2 = random.randint(1, 10)

    # Random operations
    oper = ['*', '//', '+', '-']
    ran_op = random.choice(oper)

    return f"What is {rndm1} {ran_op} {rndm2}?", rndm1, rndm2, ran_op

def process(answer, rndm1, rndm2, ran_op):
    global correct
    # Correct Answer
    if ran_op == '*':
        correct = rndm1 * rndm2
    elif ran_op == '//':
        correct = rndm1 // rndm2
    elif ran_op == '+':
        correct = rndm1 + rndm2
    elif ran_op == '-':
        correct = rndm1 - rndm2

    if answer == correct:
        return True
    else:
        return False

def get_answer():
    return screen.numinput("Answer", question_text)

# This is where all starts
ask_name()
main_display()
start_game()

def ask_question():

    global question_text, wrong_count, score

    while True:

        question_text, rndm1, rndm2, ran_op = question()

        answer = get_answer()

        if process(answer, rndm1, rndm2, ran_op):
            print("Correct!")
            t.fd(50)  # Forward Turtle
            score += 2
            if t.ycor() >= 70:
                # 7 correct answers to for perfect score
                print("You survived!!")
                score_append()
                win.showturtle()
                t.hideturtle()
                s.hideturtle()
                time.sleep(5)
                screen.bye()
                main_terminal()
        else:
            print("Wrong!")
            print(f"The correct answer is {correct}")
            t.back(20)
            wrong_count += 1
            score -= 3

            if wrong_count == 2:
                sx_move = t.xcor() - 80
                sy_move = t.ycor() - 80
                s.goto(sx_move, sy_move)
            elif wrong_count == 4:
                sx_move = t.xcor() - 50
                sy_move = t.ycor() - 50
                s.goto(sx_move, sy_move)
            elif wrong_count == 5:
                s.goto(t.xcor(), t.ycor())
                t.hideturtle()
                print("You are eaten")
                time.sleep(1)
                s.hideturtle()
                eaten.showturtle()
                score_append()
                time.sleep(3)
                screen.bye()
                main_terminal()

            if t.ycor() < -200:
                print("You drowned!\n\n")
                t.hideturtle()
                drown.showturtle()
                time.sleep(3)
                screen.bye()
                main_terminal()


def main_terminal():
    print("<<<<<<<<<< Main Menu >>>>>>>>>>")
    print("""  ||  [Enter]  EXIT GAME     ||
  ||  [L]     LEADERBOARD    ||""")
    decision = input("-")

    if not decision:
        exit(123)
    elif decision.upper() =='L':
        score_display()
    else:
        enter = input("\n-- Error !! Please try again --")
        print()
        main_terminal()


turtle.done()