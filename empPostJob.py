from tkinter import*
from PIL import ImageTk 
from tkinter import messagebox
import pymysql  
import mysql.connector
# from database import connect_db

def backhomepage():
    root.destroy()
    import empHome

def on_enter(event):
    if jobTitle.get()=='JOB TITLE':
        jobTitle.delete(0,END)


def on_enter_company(event):
    if company.get()=='COMPANY':
        company.delete(0,END)


def on_enter_location(event):
    if location.get()=='LOCATION':
        location.delete(0,END)


def on_enter_salary(event):
    if salary.get()=='SALARY':
        salary.delete(0,END)


def on_enter_desc(event):
    if desc.get()=='DESCRIPTION':
        desc.delete(0,END)


def add_job():
     if jobTitle.get()=='' or company.get()=='' or location.get()=='' or salary.get()=='' or desc.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
    
     else:
        try:
            con = pymysql.connect(host='localhost' , user='root' , password='123456')
            mycursor=con.cursor()
        except:
            messagebox.showerror('error' , 'database connectivity issues please try again')
            return
        
        try:
            # query='CREATE DATABASE jobmatrix'
            # mycursor.execute(query)
            query='USE jobmatrix'
            mycursor.execute(query)
            # query='CREATE TABLE User(id INT AUTO INCREMENT PRIMARY KEY NOT NULL,name VARCHAR(50) NOT NULL,email VARCHAR(100) UNIQUE,Phone VARCHAR(20),password varchar(25),CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
            # mycursor.execute(query)
        except:
              query='USE jobmatrix'
              mycursor.execute(query)

        query='SELECT * FROM jobs where location=%s'
        # mycursor.execute(query,(location.get(),salary.get()))
        query='INSERT INTO jobs(job_title,company,description,salary,location) values(%s,%s,%s,%s,%s)'
        mycursor.execute(query,(jobTitle.get(),company.get(),desc.get(),salary.get(),location.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','job posted successfully')
        
        root.destroy()
        import empHome
       
           

    #  def clear():
    #         jobTitle.delete(0,END)
    #         company.delete(0,END)
    #         salary.delete(0,END)
    #         location.delete(0,END)
    #         desc.delete(0,END)

  
root=Tk()
root.geometry('861x461+50+50')
root.resizable(0,0)
root.title = "UserSignIn"
bg1 = ImageTk.PhotoImage(file="images/post_job.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

# jobTitlelb=Label(root,text="JOB TITLE",font=('Segoe UI Symbol',15,'bold'),bg="#d3e7ee")
# jobTitlelb.place(x=95,y=120)

jobTitle = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg="#70a8bc")
jobTitle.place(x=100,y=120)
jobTitle.insert(0,'JOB TITLE')
jobTitle.bind('<FocusIn>',on_enter)

company = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg="#70a8bc")
company.place(x=100,y=170)
company.insert(0,'COMPANY')
company.bind('<FocusIn>',on_enter_company)

location = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg="#70a8bc")
location.place(x=100,y=220)
location.insert(0,'LOCATION')
location.bind('<FocusIn>',on_enter_location)


salary = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg="#70a8bc")
salary.place(x=500,y=120)
salary.insert(0,'SALARY')
salary.bind('<FocusIn>',on_enter_salary)

desc = Entry(root,width=25,font=('Segoe UI Symbol',11,'bold'),bd=0,fg="black",bg="#70a8bc")
desc.place(x=500,y=170,height=50)
desc.insert(0,'DESCRIPTION')
desc.bind('<FocusIn>',on_enter_desc)

#creating the back button
backicon=PhotoImage(file='icons/back.png')
backbtn=Button(root,image=backicon,bd=0,cursor='hand2',fg="black",bg="white",command=backhomepage)
backbtn.place(x=10,y=415)

post=Button(root,text='POST',font=('Segoe UI Symbol',9,'bold'),fg='white',bg='blue',cursor='hand2',bd=0,activebackground='white',command=add_job)
post.place(x=345,y=330,height=30,width=120)
root.mainloop()