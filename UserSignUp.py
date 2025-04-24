from tkinter import *
from PIL import ImageTk
import pymysql
import re
from tkinter import messagebox

# Function to validate email format
def is_valid_email(email):
    email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-zA-Z]{3,}$'
    return re.match(email_pattern, email)

# Function to validate password (at least 4 characters)
def is_valid_password(password):
    return len(password) >= 4

# Function to validate phone number (10 digits)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Function to connect to the database and handle signup
def connect_database():
    user_name = username.get()
    user_email = email.get()
    user_phone = phone.get()
    user_password = password.get()
    confirm_password = confirmpass.get()

    if not all([user_name, user_email, user_phone, user_password, confirm_password]):
        messagebox.showerror('Error', 'All Fields Are Required')
        return

    if not is_valid_email(user_email):
        messagebox.showerror('Error', 'Invalid Email Format')
        return

    if not is_valid_phone(user_phone):
        messagebox.showerror('Error', 'Phone number must be 10 digits and numeric.')
        return

    if not is_valid_password(user_password):
        messagebox.showerror('Error', 'Password must be at least 4 characters long.')
        return

    if user_password != confirm_password:
        messagebox.showerror('Error', 'Password and Confirm Password should be the same')
        return

    try:
        con = pymysql.connect(host='localhost', user='root', password='123456')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error', 'Database connectivity issue. Please try again.')
        return

    try:
        mycursor.execute('CREATE DATABASE IF NOT EXISTS jobmatrix')
        mycursor.execute('USE jobmatrix')
        mycursor.execute('''
            CREATE TABLE IF NOT EXISTS User(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE,
                phone VARCHAR(20),
                password VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    except:
        mycursor.execute('USE jobmatrix')

    mycursor.execute('SELECT * FROM User WHERE email = %s', (user_email,))
    row = mycursor.fetchone()

    if row:
        messagebox.showerror('Error', 'Email already exists')
    else:
        mycursor.execute('INSERT INTO User(name, email, phone, password) VALUES(%s, %s, %s, %s)',
                         (user_name, user_email, user_phone, user_password))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Account created successfully')
        clear()
        root.destroy()
        import userSignIn

# Function to clear input fields
def clear():
    username.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    password.delete(0, END)
    confirmpass.delete(0, END)

# Placeholder functions
def on_enter_name(event):
    if username.get() == 'Username':
        username.delete(0, END)

def on_enter_email(event):
    if email.get() == 'Email_Id':
        email.delete(0, END)

def on_enter_phone(event):
    if phone.get() == 'Phone no.':
        phone.delete(0, END)

def pass_enter(event):
    if password.get() == 'password':
        password.delete(0, END)

def conpass_enter(event):
    if confirmpass.get() == 'Confirm Password':
        confirmpass.delete(0, END)

# Password toggle functions
def hide():
    eyeicon.config(file='icons/eyeclosed.png')
    password.config(show='*')
    eyebutton.config(command=show)

def show():
    eyeicon.config(file='icons/eye.png')
    password.config(show='')
    eyebutton.config(command=hide)

def hide_confirm():
    eyeicon2.config(file='icons/eyeclosed.png')
    confirmpass.config(show='*')
    eyebutton2.config(command=show_confirm)

def show_confirm():
    eyeicon2.config(file='icons/eye.png')
    confirmpass.config(show='')
    eyebutton2.config(command=hide_confirm)

def signinPage():
    root.destroy()
    import userSignIn

# GUI Setup
root = Tk()
root.geometry('671x565+50+50')
root.title('User Signup')

bg1 = ImageTk.PhotoImage(file="images/signupBG.png")
bglabel = Label(root, image=bg1)
bglabel.place(x=0, y=0)

username = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black", bg='white')
username.place(x=80, y=110)
username.insert(0, 'Username')
username.bind('<FocusIn>', on_enter_name)

email = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
email.place(x=80, y=150)
email.insert(0, 'Email_Id')
email.bind('<FocusIn>', on_enter_email)

phone = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
phone.place(x=80, y=190)
phone.insert(0, 'Phone no.')
phone.bind('<FocusIn>', on_enter_phone)

password = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
password.place(x=80, y=230)
password.insert(0, 'password')
password.bind('<FocusIn>', pass_enter)

confirmpass = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
confirmpass.place(x=80, y=270)
confirmpass.insert(0, 'Confirm Password')
confirmpass.bind('<FocusIn>', conpass_enter)

eyeicon = PhotoImage(file='icons/eye.png', height=20, width=25)
eyebutton = Button(root, image=eyeicon, bd=0, bg="white", cursor='hand2', command=hide)
eyebutton.place(x=280, y=230)

eyeicon2 = PhotoImage(file='icons/eye.png', height=20, width=25)
eyebutton2 = Button(root, image=eyeicon2, bd=0, bg="white", cursor='hand2', command=hide_confirm)
eyebutton2.place(x=280, y=270)

signUpbt = Button(root, text='SignUp', font=('Segoe UI Symbol', 10, 'bold'), fg='white', bg='green', cursor='hand2', bd=0, command=connect_database)
signUpbt.place(x=80, y=320, height=30, width=230)

signInbt = Button(root, text='SignIn', font=('Segoe UI Symbol', 9, 'bold'), fg='white', bg='green', cursor='hand2', bd=0, activebackground='#81CE81', command=signinPage)
signInbt.place(x=260, y=500, height=30, width=100)

root.mainloop()
