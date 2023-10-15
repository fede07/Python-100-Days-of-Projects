from tkinter import *

FONT = ("Arial", 11)

def miles_to_km(miles):
    return miles * 1.6093

def convert():
    miles = float(entry.get())
    kms = miles_to_km(miles)
    result_label.config(text=f"{kms}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

isEqualTo_label = Label(text="is equal to", font=FONT)
isEqualTo_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(text="", font=FONT)
result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=FONT, command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()