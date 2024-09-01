from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os
import time
import operator
import random


def show_frame(frame):

   
    frame.tkraise()


def check_username_input():
    username_input = username_entry.get()
    if username_input.strip() =="":
        messagebox.showwarning("Input Error","username has been left blank please input your username to continue")
    else:


           

        show_frame(rule_window)    
 

#def start():

root = Tk() # Tk is window, some people use root but I like window



container = Frame(root)
container.pack(fill='both', expand=True)




#title of the gui
root.title("Math Royal")

root.geometry("600x300")
#Background color of the gui

window = Frame(container, bg="#aed8f5")


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


username_label = Label(window, text="username:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

username_entry.bind('<Return>', lambda event: continue_to_game_button.invoke())



continue_to_game_button = Button(window, text="Continue to math game", command= check_username_input)
continue_to_game_button.pack()


   


# ADD TIME WINDOW
#def add_time():
#global rule_window

rule_window = Frame(container, bg = "#faf484")



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






window2_button = Button(rule_window, text="return to home", command= lambda: show_frame(window))
window2_button.pack()

playgame_button = Button(rule_window, text="play math game", command=lambda: (show_frame(game_window), reset_timer1()))
playgame_button.pack()




time_15sec_button = Button(rule_window, text="15 seconds", command=lambda: (show_frame(game_window), reset_timer15()))
time_15sec_button.place(x=150, y=250)

time_30sec_button = Button(rule_window, text="30 seconds", command=lambda: (show_frame(game_window), reset_timer30()))
time_30sec_button.place(x=250, y=250)

time_1min_button = Button(rule_window, text="1 minute", command=lambda: (show_frame(game_window), reset_timer1()))
time_1min_button.place(x=350, y=250)




def check_input():
    global score
    user_input = answer_entry.get()


    try:
       
        user_input = float(user_input)
       
        if user_input == answer:
            result_label.config(text="correct", fg ="green")
            score +=1
            score_label.config(text=f"Score: {score}")
            label.config(text=f"Good job you got {answer}")
            window4_label1.config(text=f"Score: {score}")

            brandon()
        else:
            result_label.config(text="wrong", fg = "red")
            score +=0
            score_label.config(text=f"Score: {score}")
            label.config(text=f"The correct answer was {answer}")
            window4_label1.config(text=f"Score: {score}")

            brandon()
           
    except ValueError:
        result_label.config(text="Please enter a valid number" ,fg="orange")
        score_label.config(text=f"Score: {score}")
        label.config(text=f"")
        window4_label1.config(text=f"Score: {score}")


   

def brandon():
    global number1, number2, answer
    while True:
       
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            answer = number1 + number2
        elif operation == '-':
            answer = number1 - number2
        elif operation == '*':
            answer = number1 * number2
        elif operation == '/':

            if number2 == 0 :
                continue
           
            answer = round(number1 / number2, 2)


            if len(str(answer).split('.')[1]) > 1:
                continue

        break
       
    feedback_label.config(text=f"{number1} {operation} {number2}")
   
    answer_entry.delete(0, END)

   




score =0





end_screen_window = Frame(container, bg="grey")

window4_button1 = Button(end_screen_window, text="return to home", command = lambda: show_frame(window))
window4_button1.pack()

window4_label1 = Label(end_screen_window, text=f"Score: {score}")
window4_label1.pack()






min1_timer = 60


def reset_timer1():
    global min1_timer
    min1_timer=60
    
    minus1()

def minus1():
    global min1_timer
    if min1_timer >0:
       
        min1_timer-=1
        timer_label.config(text=f"Time remaining: {min1_timer} seconds")
        root.after(1000, minus1)        
    if min1_timer == 0:
        print("times up")
        show_frame(end_screen_window)




min30_timer = 30


def reset_timer30():
    global min30_timer
    min30_timer=30
    
    minus30()

def minus30():
    global min30_timer
    if min30_timer >0:
       
        min30_timer-=1
        timer_label.config(text=f"Time remaining: {min30_timer} seconds")
        root.after(1000, minus30)        
    if min30_timer == 0:
        print("times up")
        show_frame(end_screen_window)






min15_timer = 15

def reset_timer15():
    global min15_timer
    min15_timer=15
    
    minus15()

def minus15():
    global min15_timer
    if min15_timer >0:
       
        min15_timer-=1
        timer_label.config(text=f"Time remaining: {min15_timer} seconds")
        root.after(1000, minus15)
    if min15_timer == 0:
        print("times up")
        show_frame(end_screen_window)


# PLAY GAME WINDOW

game_window = Frame(container, bg = "white")


window3_label = Label(game_window, text="hello this is the play game window")
window3_label.pack()
window3_button = Button(game_window, text="return to add time", command = lambda: show_frame(rule_window))
window3_button.pack()
window3_button2 = Button(game_window, text="return to home", command = lambda: show_frame(window))
window3_button2.pack()

window3_label = Label(game_window, text="Math Game")
window3_label.pack()

timer_label = Label(game_window, text = f"Time remaining: {min1_timer} seconds")
timer_label.pack()


problem_label = Label(game_window, text="", font=("Arial", 16))
problem_label.pack()

answer_entry = Entry(game_window)
answer_entry.pack()

submit_button = Button(game_window, text="Submit", command=check_input)
submit_button.pack()


answer_entry.bind('<Return>', lambda event: submit_button.invoke())




feedback_label = Label(game_window, text="", font=("Arial", 12))
feedback_label.pack()

score_label = Label(game_window, text="", font=("Arial", 12))
score_label.pack()


result_label = Label(game_window, text="")
result_label.pack()

label = Label(game_window, text="")
label.pack()





brandon()



for frame in (window, rule_window, game_window, end_screen_window):
    frame.place(relwidth=1, relheight=1)




show_frame(window)




root.mainloop()







 # ends the code loop
