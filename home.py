from tkinter import*
from PIL import ImageTk     #pil python image lib

root=Tk()
root.geometry('819x461+50+50')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/home1.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

# signupbt=Button(root,text='a',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='green',cursor='hand2',bd=0,activebackground='#81CE81',command=signupPage)
# signupbt.place(x=480,y=485,height=30,width=150)

root.mainloop()
