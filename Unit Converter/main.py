from tkinter import *

window = Tk()
window.config(padx=20, pady=20)

# first row
user_entry = Entry()
user_entry.grid(row=1, column=2)

mile_label = Label(text="Miles")
mile_label.grid(row=1, column=3)
mile_label.config(width=10)

# Second row
label = Label(text="is equal to")
label.grid(row=2, column=1)
label.config(width=10)

output = Label(text="0")
output.grid(row=2, column=2)

mile_label = Label(text="Km")
mile_label.grid(row=2, column=3)
mile_label.config(width=10)


# third row
def Mile_to_Kilometer():
    mile = int(user_entry.get())
    kilometer = mile * 1.6
    output.config(text=f"{kilometer}")


button = Button(text="Calculate", command=Mile_to_Kilometer)
button.grid(row=3, column=2)

window.mainloop()
