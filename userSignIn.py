import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from tkinter import*
from PIL import ImageTk


# Function to connect to MySQL database
def connect_db():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="jobmatrix")
        return conn
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# Function to authenticate user
def login_pageDB():
    if email.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            conn = connect_db()
            if conn is None:
                return

            cursor = conn.cursor()
            query = 'SELECT id FROM User WHERE email=%s AND password=%s'
            cursor.execute(query, (email.get(), password.get()))

            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror('Error', 'Invalid email or password')
            else:
                user_id = row[0]  # Get user ID from database
                messagebox.showinfo("Welcome", "WELCOME TO JOB MATRIX")
                
                root.destroy()  # Close login window
                import UserHome 
                # Set user ID in userHome 
                UserHome.set_user_id(user_id)
                 # Open the home page

        except Exception as e:
            messagebox.showerror("Error", f"Database connectivity issue: {e}")

def backHomepage():
    root.destroy()
    import welcome

def signupPage():
    root.destroy()
    import UserSignUp

def on_enter(event):
    if email.get()=='Email_Id':
        email.delete(0,END)

def pass_enter(event):
    if password.get()=='password':
        password.delete(0,END)

# Create login window
root = tk.Tk()
root.geometry('643x562+50+50')
root.title("User Login")

# Background image
bg1 = ImageTk.PhotoImage(file="images/bg2.png")
bglabel = tk.Label(root, image=bg1)
bglabel.place(x=0, y=0)

# Email field
email = tk.Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black")
email.place(x=350, y=200)
email.insert(0, 'Email_Id')

email.bind('<FocusIn>',on_enter)

# Password field
password = tk.Entry(root, width=25, font=('Segoe UI Symbol', 11, 'bold'), bd=0, fg="black", show="*")
password.place(x=350, y=250)
password.insert(0, 'password')

password.bind('<FocusIn>',pass_enter)

# Sign-in button
signinbt = tk.Button(root, text='SignIn', font=('Segoe UI Symbol', 10, 'bold'), fg='white', bg='green', cursor='hand2', bd=0, command=login_pageDB)
signinbt.place(x=350, y=325, height=30, width=230)

orLine=tk.Label(root,text="----------------OR----------------",font=('Segoe UI Symbol',16,'bold'),fg="green",bg="#81CE81")
orLine.place(x=300,y=398)

signup=tk.Label(root,text="Dont have an account?",font=('Segoe UI Symbol',11,'bold'),fg="green",bg="#81CE81")
signup.place(x=300,y=485)

signupbt=tk.Button(root,text='Create Account',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='green',cursor='hand2',bd=0,activebackground='#81CE81',command=signupPage)
signupbt.place(x=480,y=485,height=30,width=150)

# creating back button
backicon=tk.PhotoImage(file='icons/back.png')
backbtn=tk.Button(root,image=backicon,bd=0,cursor='hand2',fg="black",bg="white",command=backHomepage)
backbtn.place(x=10,y=10)

root.mainloop()
