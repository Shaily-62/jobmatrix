from tkinter import *
from PIL import ImageTk
import pymysql
import re
from tkinter import messagebox

# Function to validate email format
def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

# Function to validate password (at least 4 characters)
def is_valid_password(password):
    return len(password) >= 4  # Minimum password length of 4

# Database connection and signup
def connect_database():
    user_name = username.get()
    user_email = email.get()
    user_phone = phone.get()
    user_password = password.get()
    confirm_password = confirmpass.get()

    # Validate empty fields
    if not all([user_name, user_email, user_phone, user_password, confirm_password]):
        messagebox.showerror('Error', 'All Fields Are Required')
        return

    # Validate email format
    if not is_valid_email(user_email):
        messagebox.showerror('Error', 'Invalid Email Format')
        return

    # Validate password length
    if not is_valid_password(user_password):
        messagebox.showerror('Error', 'Password must be at least 4 characters long.')
        return

    # Validate matching passwords
    if user_password != confirm_password:
        messagebox.showerror('Error', 'Password and Confirm Password should be the same')
        return

    # Database connection
    try:
        con = pymysql.connect(host='localhost', user='root', password='123456')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error', 'Database connectivity issue. Please try again.')
        return

    try:
        mycursor.execute('USE jobmatrix')
    except:
        messagebox.showerror('Error', 'Database jobmatrix not found. Please create the database first.')
        return

    # Check if email already exists
    mycursor.execute('SELECT * FROM Employer WHERE email=%s', (user_email,))
    row = mycursor.fetchone()

    if row:
        messagebox.showerror('Error', 'Email already exists')
    else:
        mycursor.execute('INSERT INTO Employer(Name, Email, Phone, Password) VALUES (%s, %s, %s, %s)',
                         (user_name, user_email, user_phone, user_password))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Account created successfully')
        clear()
        root.destroy()
        import empsignin  # Redirect to Sign In Page

# Function to clear input fields
def clear():
    username.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    password.delete(0, END)
    confirmpass.delete(0, END)

# Placeholder functions
def on_enter_name(event):
    if username.get() == 'Name':
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

def hide():
    eyeicon.config(file='icons/eyeclosed.png')
    password.config(show='*')
    eyebutton.config(command=show)

def show():
    eyeicon.config(file='icons/eye.png')
    password.config(show='')
    eyebutton.config(command=hide)

def signinPage():
    root.destroy()
    import empsignin

# GUI Setup
root = Tk()
root.geometry('861x461+50+50')
root.title('User Signup')

# Background Image
bg1 = ImageTk.PhotoImage(file="images/empsignup.png")
bglabel = Label(root, image=bg1)
bglabel.place(x=0, y=0)

# Input Fields
username = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black", bg='white')
username.place(x=110, y=140)
username.insert(0, 'Name')
username.bind('<FocusIn>', on_enter_name)

email = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
email.place(x=110, y=170)
email.insert(0, 'Email_Id')
email.bind('<FocusIn>', on_enter_email)

phone = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
phone.place(x=110, y=200)
phone.insert(0, 'Phone no.')
phone.bind('<FocusIn>', on_enter_phone)

password = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
password.place(x=110, y=230)
password.insert(0, 'password')
password.bind('<FocusIn>', pass_enter)

confirmpass = Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
confirmpass.place(x=110, y=260)
confirmpass.insert(0, 'Confirm Password')
confirmpass.bind('<FocusIn>', conpass_enter)

# Show/Hide Password Button
eyeicon = PhotoImage(file='icons/eye.png', height=20, width=25)
eyebutton = Button(root, image=eyeicon, bd=0, bg="white", cursor='hand2', command=hide)
eyebutton.place(x=310, y=230)

# Signup Button
signUpbt = Button(root, text='SignUp', font=('Segoe UI Symbol', 10, 'bold'), fg='white', bg='blue', cursor='hand2', bd=0, command=connect_database)
signUpbt.place(x=110, y=300, height=30, width=230)

# Signin Button
signInbt = Button(root, text='SignIN', font=('Segoe UI Symbol', 9, 'bold'), fg='white', bg='blue', cursor='hand2', bd=0, activebackground='#81CE81', command=signinPage)
signInbt.place(x=320, y=415, height=30, width=100)

root.mainloop()
