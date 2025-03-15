from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql                #pip install pymysql
from tkinter import messagebox

#database connection
def connect_database():
    if username.get()=='' or email.get()=='' or phone.get()=='' or password.get()=='' or confirmpass.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')

    elif password.get() != confirmpass.get():
        messagebox.showerror('error','Password and confirm password should be same')
    
    else:
        try:
            con = pymysql.connect(host='localhost' , user='root' , password='123456')
            mycursor=con.cursor()
        except:
            messagebox.showerror('error' , 'database connectivity issues please try again')
            return
        
        try:
            # query='CREATE DATABASE jobmatrix'
            # mycursor.execute(query)
            query='USE jobmatrix'
            mycursor.execute(query)
            # query='CREATE TABLE User(id INT AUTO INCREMENT PRIMARY KEY NOT NULL,name VARCHAR(50) NOT NULL,email VARCHAR(100) UNIQUE,Phone VARCHAR(20),password varchar(25),CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
            # mycursor.execute(query)
        except:
              query='USE jobmatrix'
              mycursor.execute(query)

        query='SELECT * FROM Employer where email=%s'
        mycursor.execute(query,(email.get()))
        row = mycursor.fetchone()

        # checking email exist or not 
        if row != None:
            messagebox.showerror('Error','email already exists')

        else:
            query='INSERT INTO Employer(Name,Email,Phone,password) values(%s,%s,%s,%s)'
            mycursor.execute(query,(username.get(),email.get(),phone.get(),password.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Account created Successfully')
            clear()     #we created clear function to clear all the data after the signin fron input fields
            root.destroy()
            import empsignin

# difining the function
def clear():
    username.delete(0,END)
    email.delete(0,END)
    phone.delete(0,END)
    password.delete(0,END)
    confirmpass.delete(0,END)

def on_enter_name(event):
    if username.get()=='Name':
        username.delete(0,END)

def on_enter(event):
    if email.get()=='Email_Id':
        email.delete(0,END)

def on_enter_phone(event):
    if phone.get()=='Phone no.':
        phone.delete(0,END)

def pass_enter(event):
    if password.get()=='password':
        password.delete(0,END)

def conpass_enter(event):
    if confirmpass.get()=='Confirm Password':
        confirmpass.delete(0,END)

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
 

root=Tk()
root.geometry('861x461+50+50')
# root.resizable(0,0)
root.title = "UserSignup"
bg1 = ImageTk.PhotoImage(file="images/empsignup.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

username = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg='white')
username.place(x=110,y=140)
username.insert(0,'Name')
username.bind('<FocusIn>',on_enter_name)

email = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
email.place(x=110,y=170)
email.insert(0,'Email_Id')
email.bind('<FocusIn>',on_enter)

phone = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
phone.place(x=110,y=200)
phone.insert(0,'Phone no.')
phone.bind('<FocusIn>',on_enter_phone)

password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=110,y=230)
password.insert(0,'password')
password.bind('<FocusIn>',pass_enter)

confirmpass = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
confirmpass.place(x=110,y=260)
confirmpass.insert(0,'Confirm Password')
confirmpass.bind('<FocusIn>',conpass_enter)


# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=20,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=310,y=230)


signUpbt=Button(root,text='SignUp',font=('Segoe UI Symbol',10,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,command=connect_database)
signUpbt.place(x=110,y=300,height=30,width=230)


# =======
signInbt=Button(root,text='SignIN',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,activebackground='#81CE81',command=signinPage)
signInbt.place(x=320,y=415,height=30,width=100)
# >>>>>>> de198f0887cf8b5d4476132906e18bacfc5f73f7
root.mainloop()
