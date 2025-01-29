from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
from typing import TextIO

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()
    new_data = {
        web_entry: {
            'email': email_entry,
            'password': password_entry
        }}

    if len(web_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title='Oops', message='Please enter all the fields.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)           #reading old data
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)   #updating old data with new data

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)         #saving updated data
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

#-------------------------Find PASSWORD --------------------------_------#

def find_password():
    website_entry = website_input.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found.')
    else:
        if website_entry in data:
            email = data[website_entry]['email']
            password = data[website_entry]['password']
            messagebox.showinfo(title=website_entry, message=f'Email:{email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website_entry} exists.')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager Using GUI')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'prathyusha@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_button = Button(text='Generate Password',command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()

# is_ok = messagebox.askokcancel(title=web_entry, message=f'These are the details entered: \n Email: {email_entry} '
#                                             f'\nPassword: {password_entry} \n IS it ok to save?')
# if is_ok:

# f.write(f'{web_entry} | {email_entry} | {password_entry}\n')