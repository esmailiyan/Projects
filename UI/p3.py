#importing libraries
from tkinter import *

# building a window
window = Tk()

#adding window title
window.title("Mahdi gui app")

def push():
    print(w.get())

#making vertical scale widget with scale of 0 to 100
w = Scale(from_=0, to=100)
w.pack(pady=10)

#making a button to get the value
Button(window,text="get value",command=push).pack()


#creating the loop for the program
window.mainloop()
