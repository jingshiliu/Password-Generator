from tkinter import *
from tkinter import messagebox
import random_password


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

    if website_info == '' or pwd_info == '' or email_username_info == '':
        messagebox.showwarning(title='Warning', message='Please fill out all the entries.')
    else:
        ok_to_save = messagebox.askokcancel(title=website_info,
                                            message=f'These are the details entered:\n Website: {website_info}\n'
                                                    f'Email: {email_username_info}\n '
                                                    f'Password: {pwd_info}\n Are you sure?')
        if ok_to_save:
            with open('data.txt', 'a') as data:
                data.write(f'\n{website_info} / {email_username_info} / {pwd_info}')
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)


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
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
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

window.mainloop()
