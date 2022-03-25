import json
from tkinter import *
from tkinter import messagebox
import random_password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = random_password.generate_password()
    pwd_entry.delete(0, END)
    pwd_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    website_info = website_entry.get()
    email_username_info = email_username_entry.get()
    pwd_info = pwd_entry.get()
    new_data = {website_info: {
        'email': email_username_info,
        'password': pwd_info
    }}

    if website_info == '' or pwd_info == '' or email_username_info == '':
        messagebox.showwarning(title='Warning', message='Please fill out all the entries.')
    else:
        ok_to_save = messagebox.askokcancel(title=website_info,
                                            message=f'These are the details entered:\n Website: {website_info}\n'
                                                    f'Email: {email_username_info}\n '
                                                    f'Password: {pwd_info}\n Are you sure?')
        if ok_to_save:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)

                    if website_info in data:
                        if messagebox.askokcancel(title=website_info, message="This website is in the "
                                                                              "database. Do you want to "
                                                                              "overwrite?"):
                            data.update(new_data)
                    else:
                        data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                    website_entry.delete(0, END)
                    pwd_entry.delete(0, END)
            finally:
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)


# ---------------------------- Search Data ------------------------------- #


def search_data():
    website = website_entry.get()

    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    if website in data:
        email = data[website]['email']
        pwd = data[website]['password']
        messagebox.showinfo(title=f"Website: {website}", message=f"Email: {email}\nPassword: {pwd}")
    else:
        messagebox.showerror(title='Website Not Found', message="Website Not Found\n You can safely save the "
                                                                "information of this website.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=80, pady=80)
window.geometry('+800+150')

lock_canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_logo_img = PhotoImage(file='logo.png')
lock_canvas.create_image(100, 95, image=lock_logo_img)
lock_canvas.grid(row=0, column=1)
lock_canvas.grid_anchor('center')

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_username_entry = Entry(width=38)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'jingshi@email.com')

pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_pwd_button = Button(command=generate_password, text='Generate Password')
generate_pwd_button.grid(row=3, column=2)

add_button = Button(command=save_data, text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=search_data, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
