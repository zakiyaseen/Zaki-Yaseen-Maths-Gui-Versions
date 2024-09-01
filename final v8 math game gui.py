# THIS program is created by Zaki Yaseen. 
# DATE created : 26/07/2024. 
# THIS program provides students of any math skill level the opportunity to improve their maths skills through a fun, interactive and competitive maths game. 
############################################################################################################################################### 

# Zaki Yaseen Math Game GUI AS91906

# Import all nesesary modules for tkinter
from tkinter import * # Import everything from tkinter
from tkinter import ttk # Import ttk
from tkinter import messagebox # Import messagebox
import operator # Import operator
import random # Import random



# Global variables
timer_id = None # Timer identification
tree = None # Tree none
lives = 3 # Number of lives


# text file name
FILE_NAME = "mathgame_scores_data.txt" # Naming the file name Constant


# add data to the mathgame_scores_data.txt text file
def add_data():
    global username_input, score
    with open(FILE_NAME, 'a') as file:
        file.write(f"{username_input},{timer},{difficulty},{score}\n") # adds username_input, timer, difficulty, score

# reads the data in the text file
def read_data():
    global sorted_filtered_lines15_easy, sorted_filtered_lines15_medium, sorted_filtered_lines15_hard # Reading the time 15 lines
    global sorted_filtered_lines30_easy, sorted_filtered_lines30_medium, sorted_filtered_lines30_hard # Reading the time 30 lines
    global sorted_filtered_lines60_easy, sorted_filtered_lines60_medium, sorted_filtered_lines60_hard # Reading the time 60 lines

    # Read the file content
    with open('mathgame_scores_data.txt', 'r') as file:
        lines = file.readlines()

    # Filter lines where the second column is 15
    filtered_lines15_easy = [line for line in lines if line.split(',')[1] == '15' and line.split(',')[2].strip().lower() == 'easy'] # Filter lines where the third column is easy
    filtered_lines15_medium = [line for line in lines if line.split(',')[1] == '15' and line.split(',')[2].strip().lower() == 'medium'] # Filter lines where the third column is medium
    filtered_lines15_hard = [line for line in lines if line.split(',')[1] == '15' and line.split(',')[2].strip().lower() == 'hard'] # Filter lines where the third column is hard
    # Filter lines where the second column is 30
    filtered_lines30_easy = [line for line in lines if line.split(',')[1] == '30' and line.split(',')[2].strip().lower() == 'easy'] # Filter lines where the third column is easy
    filtered_lines30_medium = [line for line in lines if line.split(',')[1] == '30' and line.split(',')[2].strip().lower() == 'medium'] # Filter lines where the third column is medium
    filtered_lines30_hard = [line for line in lines if line.split(',')[1] == '30' and line.split(',')[2].strip().lower() == 'hard'] # Filter lines where the third column is hard
    # Filter lines where the second column is 60
    filtered_lines60_easy = [line for line in lines if line.split(',')[1] == '60' and line.split(',')[2].strip().lower() == 'easy'] # Filter lines where the third column is easy
    filtered_lines60_medium = [line for line in lines if line.split(',')[1] == '60' and line.split(',')[2].strip().lower() == 'medium'] # Filter lines where the third column is medium
    filtered_lines60_hard = [line for line in lines if line.split(',')[1] == '60' and line.split(',')[2].strip().lower() == 'hard'] # Filter lines where the third column is hard



    # Sort the filtered lines timer 15 by score highest to lowest
    sorted_filtered_lines15_easy = sorted(filtered_lines15_easy, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines15_medium = sorted(filtered_lines15_medium, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines15_hard = sorted(filtered_lines15_hard, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest

    # Sort the filtered lines timer 30 by score highest to lowest
    sorted_filtered_lines30_easy = sorted(filtered_lines30_easy, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines30_medium = sorted(filtered_lines30_medium, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines30_hard = sorted(filtered_lines30_hard, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest

    # Sort the filtered lines timer 60 by score highest to lowest
    sorted_filtered_lines60_easy = sorted(filtered_lines60_easy, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines60_medium = sorted(filtered_lines60_medium, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest
    sorted_filtered_lines60_hard = sorted(filtered_lines60_hard, key=lambda line: int(line.split(',')[3]), reverse=True) # Sorting the scores from highest to lowest


# Clear all data in the treeview table
def clear_treeview():
    for item in tree.get_children():
        tree.delete(item)



def time15_easy(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines15_easy:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time15_medium(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines15_medium:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time15_hard(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines15_hard:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time30_easy(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines30_easy:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time30_medium(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines30_medium:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))

def time30_hard(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines30_hard:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time60_easy(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines60_easy:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))


def time60_medium(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines60_medium:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))



def time60_hard(): # Puts filtered and sorted data into the treeview table
    clear_treeview() # Clear all data in the treeview table
    for line in sorted_filtered_lines60_hard:
        values = line.strip().split(',')
        tree.insert("", "end", values=(values[0], values[1], values[2], values[3]))



# Checks combo box entry and which button has been pressed and activates the according def fuction to put data in treeview table
def leaderboard_difficulty(button):
    selected_difficulty = combo_box_leaderboard.get() # Gets the combo_box value selected by the user
    if selected_difficulty == "":
            messagebox.showwarning("Input Error", "Please select a difficulty level") # If selected difficulty is blank then warning messagebox is shown
    elif selected_difficulty == "easy" and button['text'] == "15 seconds":
        time15_easy() # Activates time15_easy
    elif selected_difficulty == "medium" and button['text'] == "15 seconds":
        time15_medium() # Activates time15_medium
    elif selected_difficulty == "hard" and button['text'] == "15 seconds":
        time15_hard() # Activates time15_hard
    elif selected_difficulty == "easy" and button['text'] == "30 seconds":
        time30_easy() # Activates time30_easy
    elif selected_difficulty == "medium" and button['text'] == "30 seconds":
        time30_medium() # Activates time30_medium
    elif selected_difficulty == "hard" and button['text'] == "30 seconds":
        time30_hard() # Activates time30_hard
    elif selected_difficulty == "easy" and button['text'] == "1 minute":
        time60_easy() # Activates time60_easy
    elif selected_difficulty == "medium" and button['text'] == "1 minute":
        time60_medium() # Activates time60_medium
    elif selected_difficulty == "hard" and button['text'] == "1 minute":
        time60_hard() # Activates time60_hard




# Leaderboard window
def leaderboard():
    global tree, combo_box_leaderboard
    leaderboard_window = Toplevel() # Creates new window called leaderboard_window
    leaderboard_window.geometry("600x300") # Sets window geometry to 600x300
   


    tree = ttk.Treeview(leaderboard_window, columns=('Username', 'Time', 'difficulty', 'Score'), show='headings') # Treeview columns
    tree.heading('Username', text='Username') # Username heading
    tree.heading('Time', text='Time') # Time heading
    tree.heading('difficulty', text='difficulty') # Difficulty heading
    tree.heading('Score', text='Score') # Score heading
    tree.pack(fill=BOTH, expand=True)

    tree.column('Username', width=100) # Column width 100
    tree.column('Time', width=100) # Column width 100
    tree.column('difficulty', width=100) # Column width 100
    tree.column('Score', width=100) # Column width 100


    leaderboard_label = Label(leaderboard_window, text="Choose Difficulty Level") # Choose difficulty label
    leaderboard_label.pack()
   
    combo_box_leaderboard = ttk.Combobox(leaderboard_window, values=["easy", "medium", "hard"], state="readonly") # This makes the combobox have the values in it and state = readonly makes it so that the user cannot input anything random they type into the combobox
    combo_box_leaderboard.pack()
    combo_box_leaderboard.set("")


    time_15sec_button = Button(leaderboard_window, text="15 seconds", command= lambda: leaderboard_difficulty(time_15sec_button)) # 15 sec button for displaying 15 sec data in treeview table
    time_15sec_button.pack(side=LEFT, padx=150) # Button place

    time_30sec_button = Button(leaderboard_window, text="30 seconds", command=lambda: leaderboard_difficulty(time_30sec_button)) # 30 sec button for displaying 30 sec data in treeview table
    time_30sec_button.place(x=250, y=275) # Button place

    time_1min_button = Button(leaderboard_window, text="1 minute", command=lambda: leaderboard_difficulty(time_1min_button)) # 1 min button for displaying 1 min data in treeview table
    time_1min_button.place(x=350, y=275) # Button place




# Instruction manual class
class Instruction_manual:
    def __init__(self, parent):
        self.parent = parent



    def open_instruction_manual(self):
        instructions = Toplevel(self.parent) # Creates the new instruction window
        instructions.title("Instruction window") # Instruction window title
        instructions.geometry("600x300") # Instruction window width and height 600x300
        instructions.configure(bg="white") # Instruction window background color
        instructions_label = Label(instructions, bg = "white", text="Instruction Window:\n\n1. Enter your username\n\n2. Select your difficulty and time modes\n\n3. Play the maths game and try get the most answers correct within your selcted time\n\n4. Try not to get the wrong answers and lose all your hearts\n\n5. Enjoy and have fun ツ")
        instructions_label.pack() # Label.pack()
       
       
# Credit class
class Credit:
    def __init__(self, parent):
        self.parent = parent



    def open_credits(self):
        credit = Toplevel(self.parent) # Creates the new credit window
        credit.title("credit window") # Credit window title
        credit.geometry("600x300") # Credit window width and height 600x300
        credit.configure(bg="white") # Credit window background color
        credit_label = Label(credit, bg = "white", text="Credits:\n\nMade By Zaki ")
        credit_label.pack() # Label.pack()
       



def show_frame(frame):

   
    frame.tkraise() # Raise the frame




def check_username_input():
    global username_input
    username_input = username_entry.get() # Gets the input from username entry and turns it into the username_input variable
    if username_input.strip() =="":
        messagebox.showwarning("Input Error","username has been left blank please input your username to continue") # If username if left blank will show warning messagebox
    elif len(username_input.strip()) > 18:
        messagebox.showwarning("Input Error", "username must be less than 18 characters") # If username if above 18 characters it will show warning messagebox
    else:


        show_frame(rule_window) # If username is not left blank or more than 18 characters then it will change frame to rule_window      


# MAIN WINDOW

root = Tk()

container = Frame(root)
container.pack(fill='both', expand=True)

root.title("Math Royal") # Title of the gui

root.geometry("600x300") # Window geometry size

window = Frame(container, bg="#aed8f5") # Background color of the window


image = PhotoImage(file="Math Royal image with blue bg.png")  # Update the image file path accordingly
math_royal_label = Label(window, image=image)
math_royal_label.image = image  # Keep a reference to prevent garbage collection
math_royal_label.pack(pady=10) # Label.pack()




label = Label(window, text="Welcome to The Math Game")
label.pack() # Label.pack()

label = Label(window, text="The aim of this game is to get as many math questions correct before the timer runs out")
# Label.pack()

label = Label(window, text="The current Highscore is ")
# Label.pack()

label = Label(window, bg="#aed8f5", text="\n")
label.pack()

instruction_manual = Instruction_manual(root)
instruction_button = Button(window, text = "Instructions", width=9, height=1, bg = "#f7bc3b", fg = "white", font=("Comic Sans MS", 10, "bold"), command=instruction_manual.open_instruction_manual) # Command enables the open_instruction_manual def inside the instruction_manual class
instruction_button.place(x=217, y=139) # Placing the instruction manual button


credit = Credit(root)
credit_button = Button(window, text = "credits", width=9, height= 1, bg = "#fad234", fg = "white", font=("Comic Sans MS", 10, "bold"), command=credit.open_credits) # Command enables the open_credits def inside the credit class
credit_button.place(x=300 , y=139) # Placing the credit button

label = Button(window, text = "leaderboard", command = lambda: (read_data(), leaderboard())) # Command lambda is used for more than one command and read data def reads the data from the file and leaderboard def opens the leaderboard window with the treeview table
label.pack() # Label.pack()

label = Label(window, bg="#aed8f5", text="")
label.pack() # Label.pack()


username_label = Label(window, text="username:") # Username entry label
username_label.pack() # Pack the label
username_entry = Entry(window) # Username entry
username_entry.pack() # Pack entry

username_entry.bind('<Return>', lambda event: continue_to_game_button.invoke()) # Makes the return key binded to the username_entry



continue_to_game_button = Button(window, text="Continue to math game", command= check_username_input) # Command def check_username_ input makes sure username input is not left blank and is not more than 18 characters long
continue_to_game_button.pack() # Pack the button


   


# ADD TIME WINDOW

rule_window = Frame(container, bg = "#aed8f5") # Rule window frame and background color


image2 = PhotoImage(file="gradient green.png")  # Update the image file path accordingly
background_label_green = Label(rule_window, image=image2)
background_label_green.image = image  # Keep a reference to prevent garbage collection



image3 = PhotoImage(file="gradient orange.png")  # Update the image file path accordingly
background_label_orange = Label(rule_window, image=image3)
background_label_orange.image = image  # Keep a reference to prevent garbage collection


image4 = PhotoImage(file="gradient red.png")  # Update the image file path accordingly
background_label_red = Label(rule_window, image=image4)
background_label_red.image = image  # Keep a reference to prevent garbage collection



window2_label = Label(rule_window, text="hello this is the add time window")
window2_label.pack() # Label.pack()

window2_label2 = Label(rule_window, text="Select Difficulty Level")
window2_label2.pack() # Label.pack()

combo_box = ttk.Combobox(rule_window, values=["easy", "medium", "hard"], state="readonly") # This makes the combobox have the values in it and state = readonly makes it so that the user cannot input anything random they type into the combobox
combo_box.pack()
combo_box.set("")


def update_background():
    difficulty = combo_box.get() # Gets the combo_box value selected by the user

    # Removes any of the image backgrounds
    background_label_green.place_forget() # Removes the green background
    background_label_orange.place_forget() # Removes the orange background
    background_label_red.place_forget() # Removes the red background
   
   

    # Place the background image depending of what value has been selected from the combo_box
    if difficulty == "easy":
        background_label_green.place(x=0, y=0, relwidth=1, relheight=1) # Places it in the dimentions of the window
    elif difficulty == "medium":
        background_label_orange.place(x=0, y=0, relwidth=1, relheight=1) # Places it in the dimentions of the window
    elif difficulty == "hard":
        background_label_red.place(x=0, y=0, relwidth=1, relheight=1) # Places it in the dimentions of the window


combo_box.bind("<<ComboboxSelected>>", lambda event: update_background()) # Updates the background image right after selecting the difficulty from the combo_box


update_background() # Activates the def update_background


image5 = PhotoImage(file="clock image.png")  # Update the image file path accordingly
image5_label = Label(rule_window, image=image5, bg="#b3fcf9")
image5_label.image = image5  # Keep a reference to prevent garbage collection
image5_label.pack(pady=10)




window2_button = Button(rule_window, text="← return to home", width= 13, font=("Arial", 10), command= lambda: show_frame(window)) # Changed frame to home window
window2_button.place(x=0, y=0) # Place button



def difficulty_blank15():
    difficulty = combo_box.get() # Gets the combo_box value selected by the user
    if difficulty == "":
            messagebox.showwarning("Input Error", "Please select a difficulty level") # If difficulty is blank then it will show the warning messagebox
            return
    else:
        reset_timer15() # Resets timer to 15 seconds
        show_frame(game_window) # Changes frame to game window
        random_question() # Generates math questions
       


def difficulty_blank30():
    difficulty = combo_box.get() # Gets the combo_box value selected by the user
    if difficulty == "":
            messagebox.showwarning("Input Error", "Please select a difficulty level") # If difficulty is blank then it will show the warning messagebox
            return
    else:
        show_frame(game_window) # Changes frame to game window
        reset_timer30() # Resets timer to 30 seconds
        random_question() # Generates math questions
               



def difficulty_blank60():
    difficulty = combo_box.get() # Gets the combo_box value selected by the user
    if difficulty == "":
            messagebox.showwarning("Input Error", "Please select a difficulty level") # If difficulty is blank then it will show the warning messagebox
            return
    else:
        show_frame(game_window) # Changes frame to game window
        reset_timer60() # Resets timer to 60 seconds
        random_question() # Generates math questions


       
time_15sec_button = Button(rule_window, bg = "#f7bc3b", fg = "white", font=("Comic Sans MS", 10, "bold"), text="15 seconds", command= difficulty_blank15) # Activates the def difficulty_blank15 when pressed
time_15sec_button.place(x=150, y=250) # Places button in middle of the window

time_30sec_button = Button(rule_window, bg = "#f7bc3b", fg = "white", font=("Comic Sans MS", 10, "bold"), text="30 seconds", command= difficulty_blank30) # Activates the def difficulty_blank30 when pressed
time_30sec_button.place(x=250, y=250) # Places button in middle of the window

time_1min_button = Button(rule_window, bg = "#f7bc3b", fg = "white", font=("Comic Sans MS", 10, "bold"), text="1 minute", command= difficulty_blank60) # Activates the def difficulty_blank60 when pressed
time_1min_button.place(x=350, y=250) # Places button in middle of the window




def check_input():
    global score, lives
    user_input = answer_entry.get() # Gets the input from answer_entry

    # Puts what ever is in the try into a loop
    try:
       
        user_input = float(user_input) # Float makes it so that you can enter decimal inputs

        # If the answer is correct
        if user_input == answer:
            homer_simpson_angry_label.place_forget() # Removes homer anger image when user gets answer right
            homer_simpson_thumbsup_label.place(x=460, y=70) # Places homer thumbs up image when user gets right answer
            result_label.config(text="correct", fg ="green") # Updates label to correct in green text
            score +=1 # Adds 1 to the score
            score_label.config(text=f"Score: {score}") # Updates score label
            label.config(text=f"Good job you got {answer}") # Shows your answer
            window4_label1.config(text=f"Score: {score}")

            random_question() # Generates new math question
           
        # If the answer is wrong    
        else:
            homer_simpson_thumbsup_label.place_forget() # Removes homer thumbs up image when user gets wrong answer
            homer_simpson_angry_label.place(x=40, y=70) # Places homer anger image when user gets answer wrong
            result_label.config(text="wrong", fg = "red") # Updates label to wrong in red text
            score +=0 # Add 0 to the score
            score_label.config(text=f"Score: {score}") # Updates score label
            label.config(text=f"The correct answer was {answer}") # Shows your answer
            window4_label1.config(text=f"Score: {score}")
            lives -=1 # Takes 1 live away
            number_of_lives() # Activates the def number_of_lives
            if lives > 0:
                random_question() # If lives are more than 0 than generates new math question
    # If answer is not a integer or float      
    except ValueError:
        result_label.config(text="Please enter a valid number" ,fg="orange") # Updates label to please enter a valid number in orange text
        score_label.config(text=f"Score: {score}") # Updates score label
        label.config(text=f"")
        window4_label1.config(text=f"Score: {score}")




def random_question():
    global number1, number2, answer, difficulty
    difficulty = combo_box.get() # Gets the combo_box value selected by the user

    while True:
        if difficulty =="easy":
           
            number1 = random.randint(1, 10) # Number1 will be between 1 and 10
            number2 = random.randint(1, 10) # Number2 will be between 1 and 10

        elif difficulty =="medium":
            number1 = random.randint(1, 25) # Number1 will be between 1 and 25
            number2 = random.randint(1, 25) # Number2 will be between 1 and 25

        elif difficulty =="hard":
            number1 = random.randint(1, 50) # Number1 will be between 1 and 50
            number2 = random.randint(1, 50) # Number2 will be between 1 and 50

        else:
            number1 = random.randint(1, 10) # Number1 will be between 1 and 10
            number2 = random.randint(1, 10) # Number2 will be between 1 and 10
           
           

        operation = random.choice(['+', '-', '*', '/']) # Random operation

        if operation == '+':
            answer = number1 + number2 # If operation is + then answer is number1 + number2
        elif operation == '-':
            answer = number1 - number2 # If operation is - then answer is number1 - number2
        elif operation == '*':
            answer = number1 * number2 # If operation is * then answer is number1 * number2
        elif operation == '/':

            if number2 == 0 :
                continue # If number2 is equal to zero when operation is division then it will continue the loop
           
            answer = round(number1 / number2, 2) # If operation is + then answer is number1 + number2


            if len(str(answer).split('.')[1]) > 1:
                continue # This makes sure that the answer is only 1 decimal place and if it is more than one decimal place it will continue the loop
        if answer > 250:
            continue # If the answer is more than 250 then it will continue the loop

        break # Breaks the loop
    if operation == "*":
        problem_label.config(text=f"{number1} x {number2}")

    elif operation == "/":
        problem_label.config(text=f"{number1} ÷ {number2}")

    else:
       
        problem_label.config(text=f"{number1} {operation} {number2}") # Updates the math question label
   
    answer_entry.delete(0, END) # When entry button has been pressed it will delete whatever is in the entry box

   



# Score is set to zero
score =0




def reset_score():
    global score, lives
    homer_simpson_angry_label.place_forget() # Removes homer anger image when user gets answer right
    homer_simpson_thumbsup_label.place_forget() # Removes homer thumbs up image when user gets wrong answer
    lives = 3 # Lives =3 when score is being reset
    lives_label.config(text="❤︎❤︎❤︎", bg = "#aed8f5", font=("Arial", 25)) # Updates lives label
    score = 0 # Score =0 when score is being reset
    score_label.config(text=f"Score: {score}") # Updates score label
    label.config(text="")
    window4_label1.config(text=f"Score: {score}")
    result_label.config(text="")



end_screen_window = Frame(container, bg="black") # End screen window background color

house_label = Label(end_screen_window, text = "🏠", fg = "#f7bc3b", bg = "black", font=("Comic Sans MS", 15, "bold"))
house_label.pack() # Label.pack()

window4_button1 = Button(end_screen_window, text="return to home", bg = "#f7bc3b", fg = "white", font=("Comic Sans MS", 10, "bold"), command = lambda: (show_frame(window), reset_score())) # Command resets the score and changes frame to home window
window4_button1.pack() # Pack button


image8 = PhotoImage(file="game over.png")  # Update the image file path accordingly
game_over_label = Label(end_screen_window, image=image8)
game_over_label.image = image  # Keep a reference to prevent garbage collection
game_over_label.pack(pady=10)

window4_label2 = Label(end_screen_window, text="", fg = "red", bg = "black")
window4_label2.pack() # Pack label


window4_label1 = Label(end_screen_window, text=f"Score: {score}", fg = "#f7bc3b", bg = "black", font=("Comic Sans MS", 20, "bold")) # End screen score label
window4_label1.pack() # Pack label





# Timer is set to zero
timer = 0


def reset_timer60():
    global timer, timer_id, time_button_choose
    timer=60 # Timer = 60 seconds
    time_button_choose = 60 # Time button choose = 60 seconds
   
    minus1() # Activates def minus1()

def minus1():
    global timer, timer_id
    # If time is more than 1
    if timer >0:
       
        timer-=1 # Minus 1
        timer_label.config(text=f"Time remaining: {timer} seconds") # Update timer label
        timer_id = root.after(1000, minus1)        
    else:
        print("times up")
        window4_label2.config(text = "Times up")
        show_frame(end_screen_window) # Changes frame to end screen window
        timer=60 # Sets timer back to 60 seconds
        add_data() # Adds the data



# Timer set to zero
timer = 0


def reset_timer30():
    global timer, timer_id, time_button_choose
    timer=30 # Timer = 30 seconds
    time_button_choose = 30 # Time button choose = 30 seconds
    minus30() # Activates def minus30()

def minus30():
    global timer, timer_id
    # If timer is more than zero
    if timer >0:
       
        timer-=1 # Minus 1
        timer_label.config(text=f"Time remaining: {timer} seconds") # Update timer label
        timer_id = root.after(1000, minus30)        
    else:
        print("times up")
        window4_label2.config(text = "Times up")
        show_frame(end_screen_window) # Changes frame to end screen window
        timer=30 # Sets timer back to 30 seconds
        add_data() # Adds the data





# Timer set to zero
timer = 0

def reset_timer15():
    global timer, timer_id, time_button_choose
    timer=15 # Timer = 15 seconds
    time_button_choose = 15 # Timer button choose = 15 seconds
   
    minus15() # Activates def minus15()

def minus15():
    global timer, timer_id
    # If timer is more than zero
    if timer >0:
       
        timer-=1 # minus 1
        timer_label.config(text=f"Time remaining: {timer} seconds") # Update timer label
        timer_id = root.after(1000, minus15)
    else:
        print("times up")
        window4_label2.config(text = "Times up")
        show_frame(end_screen_window) # Changes frame to end screen window
        timer=15 # Sets timer back to 15 seconds
        add_data() # Adds the data




def cancel_timer():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id) # Cancels timer
        timer_id = None

   



# PLAY GAME WINDOW

game_window = Frame(container, bg = "#aed8f5") # Game window background color


image6 = PhotoImage(file="Homer Simpson thumbs up.png")  # Update the image file path accordingly
homer_simpson_thumbsup_label = Label(game_window, image=image6)
homer_simpson_thumbsup_label.image = image  # Keep a reference to prevent garbage collection


image7 = PhotoImage(file="Homer Simpson angry.png")  # Update the image file path accordingly
homer_simpson_angry_label = Label(game_window, image=image7)
homer_simpson_angry_label.image = image  # Keep a reference to prevent garbage collection



window3_button = Button(game_window, text="← return to add time", font=("Arial", 10), width = 15, command = lambda: (show_frame(rule_window), cancel_timer())) # Cancels the timer and changes frame to rule window
window3_button.place(x=0, y=0) # Place label in the top right corner

window3_label = Label(game_window, text="Math Game", bg = "#aed8f5", fg = "#5a7dfa", font=("Comic Sans MS", 15, "bold"))
window3_label.pack() # Pack label

timer_label = Label(game_window, text = f"Time remaining: {timer} seconds", bg = "#aed8f5", font=("Comic Sans MS", 13, "bold")) # Timer label
timer_label.pack() # Pack label


empty_label = Label(game_window, text="", bg = "#aed8f5", font=("Arial", 16))
empty_label.pack() # Pack label

problem_label = Label(game_window, text="", bg = "#aed8f5", font=("Arial", 20, "bold"))
problem_label.pack()# Pack label

answer_entry = Entry(game_window)
answer_entry.pack() # Pack entry


submit_button = Button(game_window, text="Submit", command=check_input) # Command checks the answer if it is correct or incorrect
submit_button.pack()


answer_entry.bind('<Return>', lambda event: submit_button.invoke()) # Binds the enter key to answer_entry




score_label = Label(game_window, text="", font=("Arial", 12))
score_label.pack() # Pack label


result_label = Label(game_window, text="")
result_label.pack() # Pack label

label = Label(game_window, text="")
label.pack() # Pack label

lives_label = Label(game_window, text="", fg= "red", bg = "white", font=("Arial", 16)) # Lives label, ofcourse the hearts have to be red color
lives_label.place(x=495, y=0) # Place on the top right of the window


def number_of_lives():
    global lives_label, lives, timer, time_button_choose
   
    if lives == 3:
        lives_label.config(text="❤❤❤", bg = "#aed8f5", font=("Arial", 25)) # If lives = 3 then lives label will update and show 3 hearts
    elif lives == 2:
        lives_label.config(text="❤❤", bg = "#aed8f5", font=("Arial", 25)) # If lives = 2 then lives label will update and show 2 hearts
    elif lives ==1:
        lives_label.config(text="❤", bg = "#aed8f5", font=("Arial", 25)) # If lives = 1 then lives label will update and show 1 hearts
    else:
        lives_label.config(text="") # If lives = 0 then lives label will update and show nothing
        print("you died, your lives are gone")
        window4_label2.config(text = "You died, all your hearts are gone")
        cancel_timer() # Cancel timer
        show_frame(end_screen_window) # Frame changes to end screen window
        if time_button_choose == 60:
            timer = 60 # If player was playing on 60 second mode timer will equal 60
        elif time_button_choose == 30:
            timer = 30 # If player was playing on 30 second mode timer will equal 30
        elif time_button_choose == 15:
            timer = 15 # If player was playing on 15 second mode timer will equal 15
        add_data() # Adds the data



number_of_lives() # Activates the def number_of_lives()  
random_question() # Activates the def random_question()


   

for frame in (window, rule_window, game_window, end_screen_window):
    frame.place(relwidth=1, relheight=1) # Frame will be placed in the size geometry of the window



show_frame(window) # Shows the frame window



root.mainloop() # Ends the code loop
