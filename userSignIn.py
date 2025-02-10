from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql     
from tkinter import messagebox

#database connection
def login_page():
     if email.get()=='' or password.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
     else:
        try:
            con = pymysql.connect(host='localhost' , user='root' , password='123456')
            mycursor=con.cursor()
        except:
            messagebox.showerror('error' , 'database connectivity issues please try again')
            return
        
        query='USE jobmatrix'
        mycursor.execute(query)
        query='SELECT * FROM User WHERE email=%s and password=%s'
        mycursor.execute(query,(email.get(),password.get()))

        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('error' , 'Invalid email and password ')
        else:
            messagebox.showinfo("welcome" , 'WELCOME TO JOB MATRIX')
            root.destroy()
            import home


# difining the function
def on_enter(event):
    if email.get()=='Email_Id':
        email.delete(0,END)

def pass_enter(event):
    if password.get()=='password':
        password.delete(0,END)

def hide():
    eyeicon.config(file='icons/eyeclosed.png')
    password.config(show='*')
    eyebutton.config(command=show)

def show():
    eyeicon.config(file='icons/eye.png')
    password.config(show='')
    eyebutton.config(command=hide)

def signupPage():
    root.destroy()
    import UserSignUp

# def homepage():
#     root.destroy()
#     import home

root=Tk()
root.geometry('643x562+50+50')
# root.resizable(0,0)
root.title = "UserSignIn"
# root.config(bg='#4A708B')
bg1 = ImageTk.PhotoImage(file="images/bg2.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)


email = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
email.place(x=350,y=200)
email.insert(0,'Email_Id')

email.bind('<FocusIn>',on_enter)


password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=350,y=250)
password.insert(0,'password')

password.bind('<FocusIn>',pass_enter)


# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=19,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=550,y=250)

forgetButton=Button(root,text="Forget Password?",bd=0,bg="#81CE81",cursor='hand2',font=('Segoe UI Symbol',8,'bold'))
forgetButton.place(x=485,y=280)

signinbt=Button(root,text='SignIn',font=('Segoe UI Symbol',10,'bold'),fg='white',bg='green',cursor='hand2',bd=0,command=login_page)
signinbt.place(x=350,y=325,height=30,width=230)

orLine=Label(root,text="----------------OR----------------",font=('Segoe UI Symbol',16,'bold'),fg="green",bg="#81CE81")
orLine.place(x=300,y=398)

signup=Label(root,text="Dont have an account?",font=('Segoe UI Symbol',11,'bold'),fg="green",bg="#81CE81")
signup.place(x=300,y=485)

signupbt=Button(root,text='Create Account',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='green',cursor='hand2',bd=0,activebackground='#81CE81',command=signupPage)
signupbt.place(x=480,y=485,height=30,width=150)

root.mainloop()
