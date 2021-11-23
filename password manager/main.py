import json
from tkinter import *
from tkinter import messagebox
from password_gen_fun import keygen


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    password_entry.delete(0, END)
    length = int(how_long.get())
    if length > 20 or length < 8:
        messagebox.showerror(message="Invalid Length for password")
    else:
        generated_pass = keygen(length)
        password_entry.insert(0, generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website_name = website_entry.get()
    website_user = user_name_entry.get()
    website_pass = password_entry.get()

    new_data = {
        website_name: {
            "username": website_user,
            "password": website_pass
        }
    }
    if len(website_name) == 0 or len(website_user) == 0 or len(website_pass) == 0:
        messagebox.showerror(message="Fields should not be empty")

    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the information you have entered:\nwebsite name: {website_name}"
                    f"\nuser name: {website_user}\npassword: {website_pass}",
            title=website_name
        )

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Search Data ------------------------------- #


def search():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_user = data[website_name]["username"]
            website_pass = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"username:\t{website_user}\npassword:\t{website_pass}")
    except FileNotFoundError:
        messagebox.showerror(message="There is no data yet")

    except KeyError:
        messagebox.showerror(
            message="Sorry no data for website you entered please check name of the website you Entered")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# row 1
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=2)

# row 2
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

website_entry = Entry(width=48)
website_entry.grid(row=2, column=2)
website_entry.focus()

Search_pass = Button(text="Search", width=10, command=search)
Search_pass.grid(row=2, column=3)

# row 3
user_name = Label(text="Email/Username:")
user_name.grid(row=3, column=1)

user_name_entry = Entry(width=48)
user_name_entry.grid(row=3, column=2)
user_name_entry.insert(0, "nimajelodari2002@gmail.com")

# row 4
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

password_entry = Entry(width=48)
password_entry.grid(row=4, column=2)

generate_pass = Button(text="Generate", width=10, command=generate)
generate_pass.grid(row=4, column=3)

how_long = Spinbox(from_=8, to=20, width=5)
how_long.grid(row=4, column=4)

# row 5
add_button = Button(text="Add", width=41, command=add)
add_button.grid(row=5, column=2)
window.mainloop()
