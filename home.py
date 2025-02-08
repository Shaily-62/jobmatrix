from tkinter import*
from PIL import ImageTk     #pil python image lib

root=Tk()
root.geometry('819x461+50+50')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/home5.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

# applybt=Button(root,text='Apply',font=('Segoe UI Symbol',9,'bold'),fg='black',bg='blue',cursor='hand2',bd=0,activebackground='#81CE81')
# applybt.place(x=650,y=200,height=30,width=120)

# applybt=Button(root,text='Apply',font=('Segoe UI Symbol',9,'bold'),fg='black',bg='blue',cursor='hand2',bd=0,activebackground='white')
# applybt.place(x=650,y=250,height=30,width=120)

# applybt=Button(root,text='Apply',font=('Segoe UI Symbol',9,'bold'),fg='black',bg='blue',cursor='hand2',bd=0,activebackground='white')
# applybt.place(x=650,y=300,height=30,width=120)


root.mainloop()
