from tkinter import*
from PIL import ImageTk     #pil python image lib

# difining the function
def on_enter(event):
    if username.get()=='Email_Id':
        username.delete(0,END)

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
 

root=Tk()
root.geometry('643x562+50+50')
# root.resizable(0,0)
root.title = "UserSignup"
# root.config(bg='#4A708B')
bg1 = ImageTk.PhotoImage(file="images/bg1.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

# headingLb=Label(root,text='SIGN IN',font=('Segoe UI Symbol',23,'bold'),bg="green",fg="white")
# headingLb.place(x=460,y=50)

username = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
username.place(x=350,y=200)
username.insert(0,'Email_Id')

username.bind('<FocusIn>',on_enter)


password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=350,y=250)
password.insert(0,'password')

password.bind('<FocusIn>',pass_enter)


# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=20,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=550,y=249)

forgetButton=Button(root,text="Forget Password?",bd=0,bg="#4A708B",cursor='hand2',font=('Segoe UI Symbol',9,'bold'))
forgetButton.place(x=460,y=280)

root.mainloop()
