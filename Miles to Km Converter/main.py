from tkinter import *

def miles_to_kilometer():
    miles = miles_entry.get()
    km = round(1.60934 * float(miles), 2)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=30)


# Entry
miles_entry = Entry(width=10, justify="center")
miles_entry.grid(column=1, row=0)


# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)


# Button
calculate_button = Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)


window.mainloop()
