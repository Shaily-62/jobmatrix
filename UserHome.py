from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql                #pip install pymysql


def Logout():
    root.destroy()
    import userSignIn

root=Tk()
root.geometry('861x461+50+50')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/userhome.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

logout=Button(root,text='Logout',font=('Segoe UI Symbol',10,'bold'),fg='red',cursor='hand2',bd=0,command=Logout)
logout.place(x=700,y=10,height=30,width=100)

historybtn=Button(root,bd=0,text="HISTORY",font=('Segoe UI Symbol',10,'bold'),cursor='hand2',bg="#00906d",fg="white")
historybtn.place(x=10,y=145)

settingbtn=Button(root,bd=0,text="SETTING",font=('Segoe UI Symbol',10,'bold'),cursor='hand2',bg="#00906d",fg="white")
settingbtn.place(x=100,y=145)

logouticon=PhotoImage(file='icons/logout.png')
logoutbtn=Button(root,image=logouticon,bd=0,cursor='hand2',command=Logout)
logoutbtn.place(x=790,y=10)
root.mainloop()
