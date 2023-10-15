from tkinter import *

FONT = ("Arial", 11)

def miles_to_km(miles):
    return miles * 1.609344

def convert():
    miles = float(entry.get())
    kms = miles_to_km(miles)
    label_11.config(text=f"{kms}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label_20 = Label(text="Miles", font=FONT)
label_20.grid(column=2, row=0)

label_01 = Label(text="is equal to", font=FONT)
label_01.grid(column=0, row=1)

label_21 = Label(text="Km", font=FONT)
label_21.grid(column=2, row=1)

label_11 = Label(text="", font=FONT)
label_11.grid(column=1, row=1)

button = Button(text="Calculate", font=FONT, command=convert)
button.grid(column=1, row=2)

window.mainloop()