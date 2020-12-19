#importing library
from tkinter import *
from tkinter import messagebox

#creating the window object and giving title
window = Tk()
window.title("Mahdi gui app")

#defining functions to act when buttons triggers
def show_info():
   messagebox.showinfo("Show info", "showing informations")

def show_error():
    messagebox.showerror("Show error", "showing error")
    
def show_warn():    
    messagebox.showwarning("Show warn", "showing warning")

def ask_quest():
    messagebox.askquestion("ask question", "ask question")

#making buttons to test some of message boxes    
B1 = Button(window, text = "show info", command = show_info)
B1.pack()

B2 = Button(window, text = "show error", command = show_error)
B2.pack()

B3 = Button(window, text = "show warning", command = show_warn)
B3.pack()

B4 = Button(window, text = "ask question", command = ask_quest)
B4.pack()
#making a loop for window
window.mainloop()
