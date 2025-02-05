from tkinter import*
from PIL import ImageTk     #pil python image lib

# difining the function
def on_enter(event):
    if username.get()=='username':
        username.delete(0,END)

def pass_enter(event):
    if password.get()=='password':
        password.delete(0,END)
 

root=Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title = "UserSignup"
root.config(bg='#4A708B')
# bg = ImageTk.PhotoImage(file="images/bg.jpg")
bglabel=Label(root)
bglabel.place(x=0,y=0)

headingLb=Label(root,text='SIGN IN',font=('Segoe UI Symbol',23,'bold'),bg="green",fg="white")
headingLb.place(x=460,y=50)

username = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
username.place(x=450,y=200)
username.insert(0,'username')

username.bind('<FocusIn>',on_enter)

f1=Frame(root,width=230,height=2,bg="yellow")
f1.place(x=450,y=221)

password = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black")
password.place(x=450,y=250)
password.insert(0,'password')

password.bind('<FocusIn>',pass_enter)

f2=Frame(root,width=230,height=2,bg="yellow")
f2.place(x=450,y=271)

# creating the button.
eyeicon=PhotoImage(file='icons/eye.png',height=20,width=25)
eyebutton=Button(root,image=eyeicon,bd=0,bg="white",cursor='hand2')
eyebutton.place(x=650,y=250)

root.mainloop()
