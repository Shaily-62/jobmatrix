# import mysql.connector
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# # Connect to MySQL
# def connect_db():
#     return mysql.connector.connect(
#         host="localhost", user="root", password="123456", database="jobmatrix"
#     )

# # Fetch applicants for a job
# def view_applicants():
#     job_id = entry_job_id.get()
#     job_name = entry_job_name.get()
    
#     if not job_id and not job_name:
#         messagebox.showerror("Input Error", "Please enter a Job ID or Job Name")
#         return
    
#     for row in tree_applicants.get_children():
#         tree_applicants.delete(row)
    
#     conn = connect_db()
#     cursor = conn.cursor()
    
#     query = """
#         SELECT User.id, User.name, User.email, User.phone, jobs.job_title, applications.status, applications.id, applications.canceled
#         FROM User 
#         INNER JOIN applications ON User.id = applications.users 
#         INNER JOIN jobs ON applications.job_id = jobs.id
#     """
#     params = []
    
#     if job_id:
#         query += " WHERE applications.job_id = %s"
#         params.append(job_id)
#     elif job_name:
#         query += " WHERE jobs.job_title LIKE %s"
#         params.append(f"%{job_name}%")
    
#     cursor.execute(query, tuple(params))
    
#     for row in cursor.fetchall():
#         tree_applicants.insert("", "end", values=row)
    
#     conn.close()

# # Cancel an application
# def cancel_application():
#     selected = tree_applicants.selection()
#     if selected:
#         item = tree_applicants.item(selected[0])
#         application_id = item['values'][6]  # Application ID is in the 7th column
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("UPDATE applications SET canceled = TRUE WHERE id = %s", (application_id,))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Application canceled successfully")
#         view_applicants()
#     else:
#         messagebox.showerror("Selection Error", "No application selected")

# # Accept application
# def accept_application():
#     selected = tree_applicants.selection()
#     if selected:
#         item = tree_applicants.item(selected[0])
#         application_id = item['values'][6]
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("UPDATE applications SET status = 'accepted' WHERE id = %s", (application_id,))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Application accepted successfully")
#         view_applicants()
#     else:
#         messagebox.showerror("Selection Error", "No application selected")

# # Reject application
# def reject_application():
#     selected = tree_applicants.selection()
#     if selected:
#         item = tree_applicants.item(selected[0])
#         application_id = item['values'][6]
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("UPDATE applications SET status = 'rejected' WHERE id = %s", (application_id,))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Application rejected successfully")
#         view_applicants()
#     else:
#         messagebox.showerror("Selection Error", "No application selected")

# # UI Setup
# root = tk.Tk()
# root.title("Manage Job Applications")
# root.configure(bg='#f0f0f0')

# # Input Fields
# tk.Label(root, text="Job ID", font=("Arial", 12), bg='#f0f0f0').grid(row=0, column=0, pady=5, padx=5)
# entry_job_id = tk.Entry(root, font=("Arial", 12))
# entry_job_id.grid(row=0, column=1, pady=5, padx=5)

# tk.Label(root, text="Job Name", font=("Arial", 12), bg='#f0f0f0').grid(row=1, column=0, pady=5, padx=5)
# entry_job_name = tk.Entry(root, font=("Arial", 12))
# entry_job_name.grid(row=1, column=1, pady=5, padx=5)

# # Buttons
# button_style = {"font": ("Arial", 12), "width": 20, "bg": "#007BFF", "fg": "white", "bd": 2}
# tk.Button(root, text="View Applicants", command=view_applicants, **button_style).grid(row=2, column=0, columnspan=2, pady=5)
# tk.Button(root, text="Cancel Application", command=cancel_application, **button_style).grid(row=3, column=0, columnspan=2, pady=5)
# tk.Button(root, text="Accept Application", command=accept_application, **button_style).grid(row=4, column=0, columnspan=2, pady=5)
# tk.Button(root, text="Reject Application", command=reject_application, **button_style).grid(row=5, column=0, columnspan=2, pady=5)

# # Applicants List
# tree_frame = tk.Frame(root, bg='#f0f0f0')
# tree_frame.grid(row=6, column=0, columnspan=2, pady=10)
# tree_applicants = ttk.Treeview(tree_frame, columns=("ID", "Name", "Email", "Phone", "Job Title", "Status", "Application ID", "Canceled"), show="headings")
# for col in ("ID", "Name", "Email", "Phone", "Job Title", "Status", "Application ID", "Canceled"):
#     tree_applicants.heading(col, text=col)
#     tree_applicants.column(col, width=150)
# tree_applicants.pack()

# root.mainloop()

import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os


def backHomepage():
    root.destroy()
    import empHome

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost", user="root", password="123456", database="jobmatrix"
    )

# Fetch applicants for a job
def view_applicants():
    job_id = entry_job_id.get()
    job_name = entry_job_name.get()
    
    if not job_id and not job_name:
        messagebox.showerror("Input Error", "Please enter a Job ID or Job Name")
        return
    
    for row in tree_applicants.get_children():
        tree_applicants.delete(row)
    
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
        SELECT User.id, User.name, User.email, User.phone, jobs.job_title, applications.status, applications.id, applications.canceled, User.resume_path
        FROM User 
        INNER JOIN applications ON User.id = applications.users 
        INNER JOIN jobs ON applications.job_id = jobs.id
    """
    params = []
    
    if job_id:
        query += " WHERE applications.job_id = %s"
        params.append(job_id)
    elif job_name:
        query += " WHERE jobs.job_title LIKE %s"
        params.append(f"%{job_name}%")
    
    cursor.execute(query, tuple(params))
    
    for row in cursor.fetchall():
        tree_applicants.insert("", "end", values=row)
    
    conn.close()

# View Resume
def view_resume():
    selected = tree_applicants.selection()
    if selected:
        item = tree_applicants.item(selected[0])
        resume_path = item['values'][8]  # Resume path is in the 9th column
        
        if resume_path and os.path.exists(resume_path):
            os.startfile(resume_path)  # Open the resume file
        else:
            messagebox.showerror("File Not Found", "Resume file not found or not uploaded.")
    else:
        messagebox.showerror("Selection Error", "No applicant selected")

# Cancel an application
def cancel_application():
    selected = tree_applicants.selection()
    if selected:
        item = tree_applicants.item(selected[0])
        application_id = item['values'][6]  # Application ID is in the 7th column
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET canceled = TRUE WHERE id = %s", (application_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Application canceled successfully")
        view_applicants()
    else:
        messagebox.showerror("Selection Error", "No application selected")

# Accept application
def accept_application():
    selected = tree_applicants.selection()
    if selected:
        item = tree_applicants.item(selected[0])
        application_id = item['values'][6]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET status = 'accepted' WHERE id = %s", (application_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Application accepted successfully")
        view_applicants()
    else:
        messagebox.showerror("Selection Error", "No application selected")

# Reject application
def reject_application():
    selected = tree_applicants.selection()
    if selected:
        item = tree_applicants.item(selected[0])
        application_id = item['values'][6]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET status = 'rejected' WHERE id = %s", (application_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Application rejected successfully")
        view_applicants()
    else:
        messagebox.showerror("Selection Error", "No application selected")

# UI Setup
root = tk.Tk()
root.title("Manage Job Applications")
root.configure(bg='#f0f0f0')

# Input Fields
tk.Label(root, text="Job ID", font=("Arial", 12), bg='#f0f0f0').grid(row=0, column=0, pady=5, padx=5)
entry_job_id = tk.Entry(root, font=("Arial", 12))
entry_job_id.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Job Name", font=("Arial", 12), bg='#f0f0f0').grid(row=1, column=0, pady=5, padx=5)
entry_job_name = tk.Entry(root, font=("Arial", 12))
entry_job_name.grid(row=1, column=1, pady=5, padx=5)

# Buttons
button_style = {"font": ("Arial", 12), "width": 20, "bg": "#007BFF", "fg": "white", "bd": 2}
tk.Button(root, text="View Applicants", command=view_applicants, **button_style).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Cancel Application", command=cancel_application, **button_style).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Accept Application", command=accept_application, **button_style).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Reject Application", command=reject_application, **button_style).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="View Resume", command=view_resume, **button_style).grid(row=6, column=0, columnspan=2, pady=5)  # New Button

# Applicants List
tree_frame = tk.Frame(root, bg='#f0f0f0')
tree_frame.grid(row=7, column=0, columnspan=2, pady=10)
tree_applicants = ttk.Treeview(tree_frame, columns=("ID", "Name", "Email", "Phone", "Job Title", "Status", "Application ID", "Canceled", "Resume Path"), show="headings")

for col in ("ID", "Name", "Email", "Phone", "Job Title", "Status", "Application ID", "Canceled", "Resume Path"):
    tree_applicants.heading(col, text=col)
    tree_applicants.column(col, width=150)

tree_applicants.pack()

# creating back button
backicon=tk.PhotoImage(file='icons/back.png')
backbtn=tk.Button(root,image=backicon,bd=0,cursor='hand2',fg="black",bg="white",command=backHomepage)
backbtn.place(x=10,y=10)

root.mainloop()

