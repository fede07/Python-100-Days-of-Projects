from tkinter import *

window = Tk()
window.title("New GUI")
window.minsize(width= 500, height=500)
window.config(padx=10, pady=10)

#label

my_label = Label(text="Testing", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.grid(row=0, column=0)
my_label.config(text="New Text")

#button

def button_clicked():
    print("I got clicked")
    text_ = input.get()
    my_label.config(text=text_)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button_2 = Button(text="New button")
button_2.grid(row=0, column=2)

#entry

input = Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()