from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql                #pip install pymysql
from tkinter import messagebox

#database connection
def emphome():
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
        query='SELECT * FROM Employer WHERE Email=%s and password=%s'
        mycursor.execute(query,(email.get(),password.get()))

        row = mycursor.fetchone()
        if row!=None:
            messagebox.showerror('error' , 'Invalid email and password ')
        else:
            messagebox.showinfo("welcome" , 'WELCOME TO JOB MATRIX')
            root.destroy()
            import empHome



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

def empsignupPage():
    root.destroy()
    import empsignup

root=Tk()
root.geometry('861x461+50+50')
# root.resizable(0,0)
root.title = "UserSignIn"
# root.config(bg='#4A708B')
bg1 = ImageTk.PhotoImage(file="images/empsignin.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)


email = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
email.place(x=520,y=160)
email.insert(0,'Email_Id')

email.bind('<FocusIn>',on_enter)


password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=520,y=210)
password.insert(0,'password')

password.bind('<FocusIn>',pass_enter)


# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=19,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=720,y=210)

forgetButton=Button(root,text="Forget Password?",bd=0,bg="#81CE81",cursor='hand2',font=('Segoe UI Symbol',8,'bold'))
forgetButton.place(x=635,y=240)

signinbt=Button(root,text='SignIn',font=('Segoe UI Symbol',10,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,command=emphome)
signinbt.place(x=520,y=280,height=30,width=230)

orLine=Label(root,text="--------------------OR--------------------",font=('Segoe UI Symbol',16,'bold'),fg="black",bg="deepskyblue")
orLine.place(x=440,y=350)


signupbt=Button(root,text='Create Account',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,activebackground='white',command=empsignupPage)
signupbt.place(x=715,y=415,height=30,width=120)

root.mainloop()
