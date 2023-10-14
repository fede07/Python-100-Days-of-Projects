import tkinter

window = tkinter.Tk()
window.title("New GUI")
window.minsize(width= 800, height=600)

my_label = tkinter.Label(text="testing", font=("Arial", 24, "bold"))
my_label.pack()



window.mainloop()