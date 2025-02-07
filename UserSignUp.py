from tkinter import*
from PIL import ImageTk     #pil python image lib

# difining the function
def on_enter_name(event):
    if username.get()=='Your Name':
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
 

root=Tk()
root.geometry('671x565+50+50')
# root.resizable(0,0)
root.title = "UserSignup"
bg1 = ImageTk.PhotoImage(file="images/signupBG.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

username = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg='white')
username.place(x=45,y=110)
username.insert(0,'Your Name')
username.bind('<FocusIn>',on_enter_name)

email = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
email.place(x=45,y=150)
email.insert(0,'Email_Id')
email.bind('<FocusIn>',on_enter)

phone = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
phone.place(x=45,y=190)
phone.insert(0,'Phone no.')
phone.bind('<FocusIn>',on_enter_phone)

password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=45,y=230)
password.insert(0,'password')
password.bind('<FocusIn>',pass_enter)

confirmpass = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
confirmpass.place(x=45,y=270)
confirmpass.insert(0,'Confirm Password')
confirmpass.bind('<FocusIn>',conpass_enter)


# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=20,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=240,y=230)


signUpbt=Button(root,text='SignUp',font=('Segoe UI Symbol',10,'bold'),fg='white',bg='green',cursor='hand2',bd=0)
signUpbt.place(x=65,y=320,height=30,width=150)


signInbt=Button(root,text='SignIN',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='green',cursor='hand2',bd=0,activebackground='#81CE81')
signInbt.place(x=260,y=500,height=30,width=100)

root.mainloop()
