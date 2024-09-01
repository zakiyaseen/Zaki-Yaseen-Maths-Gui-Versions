#Zaki yaseen Math Game Gui (Math Royal)


#Import tkinter and all nessesary 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os
import time
import operator
import random





#Name The file
file_name = "mathgame_scores_data.txt"

#add data
def add_data():
    global username_input, score
    with open(file_name, 'a') as file:
        file.write(f"{username_input},{score}\n") #adds username, score to the text file named mathgame_scores_data

#display the data
def display_data():
    try:
        with open(file_name, 'r') as file: #reads the data in the text file
            data = file.readlines()
            if data:
                display_text = "Leaderboard:\n"
                for line in data:
                    #print(f"Reading line: {line}")  # Debugging
                    username, score = line.strip().split(',')
                    display_text += f"Username: {username}, Score: {score}\n"
                display_data_label.config(text=display_text)

            else:
                display_data_label.config(text="No data found")

    except FileNotFoundError:
        display_data_label.config(text="No data found")
               





def show_frame(frame):

   
    frame.tkraise()

# check if username input is left blank
def check_username_input():
    global username_input
    username_input = username_entry.get() #gets username entry and turns it into the username_input variable 
    if username_input.strip() =="": # check if username_input is blank
        messagebox.showwarning("Input Error","username has been left blank please input your username to continue") #if the username_input is blank then it shows a messagebox telling the user input error , you cannot leave it blank
    else:



        show_frame(rule_window) # if username_input is not blank allows user to continue to the rule window

# MAIN WINDOW

root = Tk() # Tk is window, some people use root but I like window



container = Frame(root)
container.pack(fill='both', expand=True)




#title of the gui
root.title("Math Royal") # title of the window

root.geometry("600x300") # size of the window
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

            random_math_question()
        else:
            result_label.config(text="wrong", fg = "red")
            score +=0
            score_label.config(text=f"Score: {score}")
            label.config(text=f"The correct answer was {answer}")
            window4_label1.config(text=f"Score: {score}")

            random_math_question()
           
    except ValueError:
        result_label.config(text="Please enter a valid number" ,fg="orange")
        score_label.config(text=f"Score: {score}")
        label.config(text=f"")
        window4_label1.config(text=f"Score: {score}")


   

def random_math_question():
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




def reset_score():
    global score
    score = 0
    score_label.config(text=f"Score: {score}")
    label.config(text="")
    window4_label1.config(text=f"Score: {score}")
    result_label.config(text="")



end_screen_window = Frame(container, bg="grey")

window4_button1 = Button(end_screen_window, text="return to home", command = lambda: (show_frame(window), reset_score()))
window4_button1.pack()

window4_label1 = Label(end_screen_window, text=f"Score: {score}")
window4_label1.pack()

window4_button2 = Button(end_screen_window, text="leaderboard")
window4_button2.pack()

display_data_label = Label(end_screen_window, text="")
display_data_label.pack()




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
    else:
        print("times up")
        show_frame(end_screen_window)
        add_data()
        display_data()




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
    else:
        print("times up")
        show_frame(end_screen_window)
        add_data()
        display_data()






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
    else:
        print("times up")
        show_frame(end_screen_window)
        add_data()
        display_data()




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





random_math_question()


 
   

for frame in (window, rule_window, game_window, end_screen_window):
    frame.place(relwidth=1, relheight=1)





show_frame(window)




root.mainloop()


 # ends the code loop
