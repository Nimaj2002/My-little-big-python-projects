from tkinter import *
from tkinter import messagebox

from password_gen_fun import keygen


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    password_entry.delete(0, END)
    length = int(how_long.get())
    generated_pass = keygen(length)
    password_entry.insert(0, generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website_name = website_entry.get()
    website_user = user_name_entry.get()
    website_pass = password_entry.get()

    if len(website_name) == 0 or len(website_user) == 0 or len(website_pass) == 0:
        messagebox.showerror(message="Fields should not be empty")

    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the information you have entered:\nwebsite name: {website_name}"
                    f"\nuser name: {website_user}\npassword: {website_pass}",
            title=website_name
        )

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_name} | {website_user} | {website_pass}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

# row 1
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=2)

# row 2
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

website_entry = Entry(width=48)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

# row 3
user_name = Label(text="Email/Username:")
user_name.grid(row=3, column=1)

user_name_entry = Entry(width=48)
user_name_entry.grid(row=3, column=2, columnspan=2)
user_name_entry.insert(0, "nimajelodari2002@gmail.com")

# row 4
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

password_entry = Entry(width=48)
password_entry.grid(row=4, column=2, columnspan=2)

generate_pass = Button(text="Generate", width=10, command=generate)
generate_pass.grid(row=4, column=3)

how_long = Spinbox(from_=8, to=20, width=5)
how_long.grid(row=4, column=4)

# row 5
add_button = Button(text="Add", width=41, command=add)
add_button.grid(row=5, column=2, columnspan=2)
window.mainloop()
