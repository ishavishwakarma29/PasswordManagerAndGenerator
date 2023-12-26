# imports

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------- find password ---------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No Data File Found.")


# ------------ generate password ------------#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(0, nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(0, nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(0, nr_numbers)]
    password_list = password_numbers+password_letters+password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#  ---------------- SAVE ------------ #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else :
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try :
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
                    # saving updated data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.delete(0, END)




# --------------- UI -------------------#
window = Tk()
window.title("password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1)
website_entry.focus()

# email
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=37)
password_entry.grid(row=3, column=1)

# search button
search_button = Button(text="Search", width=14,command=find_password)
search_button.grid(row=1, column=2)

# generate_password
pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
