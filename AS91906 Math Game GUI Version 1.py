from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os
import time
#import tkinter, ttk, messagebox

def quit_pro():
    window.withdraw()
def start():
    window = Tk() # Tk is window, some people use root but I like window


    #title of the gui 
    window.title("Math Game")

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


    add_appliance_button = Button(window, text="Continue to math game", command= add_appliance)
    add_appliance_button.pack()


    window.mainloop()



def add_appliance():
    
    rule_window = Toplevel()
    rule_window.config(bg="#aed8f5")
    rule_window.geometry("400x400")
    window2_label = Label(rule_window, text="hello this is the new window")
    window2_label.pack()
    window2_button = Button(rule_window, text="Add Appliance")
    window2_button.pack()
    rule_window.mainloop()





start()



 




 # ends the code loop

