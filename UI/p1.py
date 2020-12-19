#importing libraries
from tkinter import *

#inserting items in list_box
def insert_element():
    list_box.insert(END,name_entry.get())

#function to clear all the data in list_box
def clear_box():    
    list_box.delete(0,END)

# building a window
window = Tk()

#adding window title
window.title("Mahdi gui app")

#an entry for giving the elements we want to add
name_entry = Entry(window)
name_entry.pack()

#a button to send the entries to listbox
send_btn = Button(window,text="send to box",command=insert_element)
send_btn.pack()

#a button to clear all the contents in box
send_btn = Button(window,text="clear the box",command=clear_box)
send_btn.pack()

#creating a list box for elements
list_box = Listbox(window)
list_box.pack()
#creating the loop for the program
window.mainloop()
