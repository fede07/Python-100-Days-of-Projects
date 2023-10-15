from tkinter import *

window = Tk()
window.title("New GUI")
window.minsize(width= 800, height=600)

#label

my_label = Label(text="Testing", font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label.config(text="New Text")

#button

def button_clicked():
    print("I got clicked")
    text_ = input.get()
    my_label.config(text=text_)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#entry

input = Entry(width=10)
input.pack()


window.mainloop()