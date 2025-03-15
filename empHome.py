from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql                #pip install pymysql

def Logout():
    root.destroy()
    import empsignin

def postjob():
    root.destroy()
    import empPostJob

def managejob():
    root.destroy()
    import EmpManageJobs

def viewJobs():
    root.destroy()
    import EmpViewJob

root=Tk()
root.geometry('861x461+50+50')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/emphome.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

logout=Button(root,text='Logout',font=('Segoe UI Symbol',11,'bold'),fg='red',bg="white",cursor='hand2',bd=0,command=Logout)
logout.place(x=710,y=10,height=30,width=100)

logouticon=PhotoImage(file='icons/logout.png')
logoutbtn=Button(root,image=logouticon,bd=0,cursor='hand2',bg="white",command=Logout)
logoutbtn.place(x=810,y=10,height=30)

notify=PhotoImage(file='icons/notify.png')
notifybtn=Button(root,image=notify,bd=0,cursor='hand2',bg="deepskyblue4")
notifybtn.place(x=800,y=140)

postJobbtn=Button(root,bd=0,text="POST A JOB",font=('Segoe UI Symbol',9,'bold'),cursor='hand2',bg="deepskyblue4",fg="white",command=postjob)
postJobbtn.place(x=10,y=145)

PINKpostJobbtn=Button(root,bd=0,text="POST A JOB",font=('Segoe UI Symbol',11,'bold'),cursor='hand2',bg="crimson",fg="white",command=postjob)
PINKpostJobbtn.place(x=320,y=250)

viewJobsbtn=Button(root,bd=0,text="VIEW JOBS",font=('Segoe UI Symbol',9,'bold'),cursor='hand2',bg="deepskyblue4",fg="white",command=viewJobs)
viewJobsbtn.place(x=110,y=145)

manageJobs=Button(root,bd=0,text="MANAGE JOBS",font=('Segoe UI Symbol',9,'bold'),cursor='hand2',bg="deepskyblue4",fg="white",command=managejob)
manageJobs.place(x=200,y=145)

manageCandi=Button(root,bd=0,text="MANAGE CANDIDATES",font=('Segoe UI Symbol',9,'bold'),cursor='hand2',bg="deepskyblue4",fg="white")
manageCandi.place(x=320,y=145)


root.mainloop()