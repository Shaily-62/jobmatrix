from tkinter import*
from PIL import ImageTk     #pil python image lib


def signinPage():
    root.destroy()
    import userSignIn

root=Tk()
root.geometry('819x461+100+100')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/welcome.jpg")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

#employer login button
employer=Button(root,text='Employer Login',font=('Segoe UI Symbol',14,'bold'),fg='black',bg='#007FFF',cursor='hand2',bd=0,command=signinPage)
employer.place(x=170,y=280,height=35,width=200)

#candidate login button
candidate=Button(root,text='Candidate Login',font=('Segoe UI Symbol',14,'bold'),fg='black',bg='#01bb3b',cursor='hand2',bd=0,command=signinPage)
candidate.place(x=470,y=280,height=35,width=200)

root.mainloop()
