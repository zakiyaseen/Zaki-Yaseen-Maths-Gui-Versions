from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os
import time
import operator
import random

#import tkinter, ttk, messagebox






# MAIN WINDOW
def start():
    global window
    window = Tk() # Tk is window, some people use root but I like window


    #title of the gui
    window.title("Math Royal")

    window.geometry("600x300")
    #Background color of the gui
    window.config(bg="#aed8f5")


    label = Label(window, text="Welcome to The Math Game")
    label.pack()

    label = Label(window, text="The aim of this game is to get as many math questions correct before the timer runs out")
    label.pack()

    label = Label(window, text="The current Highscore is ")
    label.pack()


    label = Label(window, bg="#aed8f5", text="")
    label.pack()
    label = Label(window, bg="#aed8f5", text="")
    label.pack()
    label = Label(window, bg="#aed8f5", text="")
    label.pack()
    label = Label(window, bg="#aed8f5", text="")
    label.pack()


    add_appliance_button = Button(window, text="Continue to math game", command= lambda: [window.withdraw(), add_time()])
    add_appliance_button.pack()


    window.mainloop()


# ADD TIME WINDOW
def add_time():
    global rule_window
   
    rule_window = Toplevel()
   
    rule_window.config(bg="#faf484")
    rule_window.geometry("600x300")
    window2_label = Label(rule_window, text="hello this is the add time window")
    window2_label.pack()

   
    # Define the smaller clock design lines
    clock_design = [
        "      ██████████      ",
        "    ██          ██    ",
        "  ██      ██      ██  ",
        "██        ██        ██",
        "██        ██        ██",
        "██        ██        ██",
        "██          ██      ██",
        "██            ██    ██",
        "  ██              ██  ",
        "    ██          ██    ",
        "      ██████████      "
    ]

    # Add each line of the clock design to the window with a smaller font size
    for line in clock_design:
        clock_label = Label(rule_window, text=line, font=("Courier", 6), bg="#faf484", justify="left")
        clock_label.pack()

   



   
    window2_button = Button(rule_window, text="return to home", command= lambda: [rule_window.withdraw(), start()])
    window2_button.pack()

    playgame_button = Button(rule_window, text="play math game", command=play_game)
    playgame_button.pack()




    time_1min_button = Button(rule_window, text="1 minute")
    time_1min_button.place(x=150, y=250)

    time_2min_button = Button(rule_window, text="2 minute")
    time_2min_button.place(x=250, y=250)

    time_3min_button = Button(rule_window, text="3 minute")
    time_3min_button.place(x=350, y=250)
    
   



   
    rule_window.mainloop()








# PLAY GAME WINDOW
def play_game():
    global game_window, problem_label, answer_entry, feedback_label, score_label
    rule_window.withdraw()
    game_window = Toplevel()
   
    game_window.config(bg="white")
    game_window.geometry("600x300")
    window3_label = Label(game_window, text="hello this is the play game window")
    window3_label.pack()
    window3_button = Button(game_window, text="return to add time", command = lambda: [game_window.withdraw(), add_time()])
    window3_button.pack()
    window3_button2 = Button(game_window, text="return to home", command = lambda: [game_window.withdraw(), start()])
    window3_button2.pack()

    window3_label = Label(game_window, text="Math Game")
    window3_label.pack()

    problem_label = Label(game_window, text="", font=("Arial", 16))
    problem_label.pack()

    answer_entry = Entry(game_window)
    answer_entry.pack()

    submit_button = Button(game_window, text="Submit", command=check_answer)
    submit_button.pack()


    # Bind the Enter key to the button's command
    game_window.bind('<Return>', lambda event: submit_button.invoke())

    

    feedback_label = Label(game_window, text="", font=("Arial", 12))
    feedback_label.pack()

    score_label = Label(game_window, text="Score: 0", font=("Arial", 12))
    score_label.pack()

    

    new_problem()
    




    


    game_window.mainloop()











def random_problem():
    operators = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
    }


    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    operation = random.choice(list(operators.keys()))
    answer = operators[operation](num_1, num_2)
    
    return num_1, operation, num_2,answer


def ask_question():
    answer = int(random_problem())
    guess = float(input('enter your answer: '))
    return guess == answer

def game():
    score = 0
    while True:
        if ask_question() == True:
            score += 1
            print('correct')
        else:
            print('Incorrect')
            break
    print(f'game over{score}')
    




 
def new_problem():
    global current_answer
    num_1, operation, num_2, answer = random_problem()
    problem_label.config(text=f"What is {num_1} {operation} {num_2}?")
    current_answer = answer

def check_answer():
    global score
    try:
        guess = float(answer_entry.get())
        if guess == current_answer:
            feedback_label.config(text="Correct!", fg="green")
            score += 1
        else:
            feedback_label.config(text=f"Incorrect! The correct answer was {current_answer}", fg="red")
            score += 0
    except ValueError:
        feedback_label.config(text="Please enter a valid number.", fg="red")
    score_label.config(text=f"Score: {score}")
    answer_entry.delete(0, END)
    new_problem()

score = 0
current_answer = 0

start()



 # ends the code loop
