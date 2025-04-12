import tkinter as tk
from tkinter import ttk
import mysql.connector

def backHomepage():
    root.destroy()
    import empHome

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="jobmatrix"
)
cursor = conn.cursor()

# GUI setup
root = tk.Tk()
root.title("Job Listings")
root.geometry('800x450')
root.configure(bg="white")  # Set background color

# Title Label
title_label = tk.Label(root, text="Available Job Listings", font=("Arial", 16, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

def fetch_jobs():
    cursor.execute("SELECT id, job_title, company, description, salary, location FROM jobs")  # Excluding emp_id
    rows = cursor.fetchall()
    for row in job_table.get_children():
        job_table.delete(row)
    for row in rows:
        job_table.insert("", "end", values=row)

# Frame for table with padding
frame = tk.Frame(root, bg="white")
frame.pack(padx=10, pady=5, expand=True, fill="both")

# Job Table (Excluding Employer ID)
columns = ("ID", "Job Title", "Company", "Description", "Salary", "Location")
job_table = ttk.Treeview(frame, columns=columns, show="headings")

# Add column headings
for col in columns:
    job_table.heading(col, text=col)
    job_table.column(col, width=120)  # Set default column width

# Apply better styling
style = ttk.Style()
style.configure("Treeview", font=("Arial", 10), rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
style.map("Treeview", background=[("selected", "#cce5ff")])  # Highlight selected row

# Scrollbars
scroll_y = ttk.Scrollbar(frame, orient="vertical", command=job_table.yview)
scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=job_table.xview)
job_table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
job_table.pack(expand=True, fill="both")

fetch_jobs()

# creating back button
backicon=tk.PhotoImage(file='icons/back.png')
backbtn=tk.Button(root,image=backicon,bd=0,cursor='hand2',fg="black",bg="white",command=backHomepage)
backbtn.place(x=10,y=10)
root.mainloop()
root.mainloop()

# Close database connection on exit
conn.close()
