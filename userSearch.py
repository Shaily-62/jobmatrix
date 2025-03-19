import tkinter as tk
from PIL import ImageTk 
from tkinter import ttk, messagebox
import pymysql

def backhomepage():
    job_search_window.destroy()
    import UserHome
  

# Global variable to store logged-in user ID
logged_in_user_id = 1  # Assuming a user is already logged in

# Function to connect to MySQL database
def connect_db():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="jobmatrix")
        return conn
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# Function to open the job search page
def open_job_search_page():
    global job_search_window, title_var, location_var, salary_var, job_list
    
    job_search_window = tk.Tk()
    job_search_window.title("Job Search")
    job_search_window.geometry("800x400")
    job_search_window.configure(bg="#f0f0f0")

    frame = ttk.Frame(job_search_window, padding=10)
    frame.pack(fill="x")

    ttk.Label(frame, text="Job Title:").grid(row=0, column=0, padx=5, pady=5)
    title_var = tk.StringVar()
    ttk.Entry(frame, textvariable=title_var).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame, text="Location:").grid(row=0, column=2, padx=5, pady=5)
    location_var = tk.StringVar()
    ttk.Entry(frame, textvariable=location_var).grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(frame, text="Min Salary:").grid(row=0, column=4, padx=5, pady=5)
    salary_var = tk.StringVar()
    ttk.Entry(frame, textvariable=salary_var).grid(row=0, column=5, padx=5, pady=5)

    ttk.Button(frame, text="Search", command=search_jobs).grid(row=0, column=6, padx=5, pady=5)

    columns = ("Job ID", "Job Title", "Location", "Salary")
    job_list = ttk.Treeview(job_search_window, columns=columns, show="headings")
    for col in columns:
        job_list.heading(col, text=col)
        job_list.column(col, width=150)
    job_list.pack(fill="both", expand=True)

    ttk.Button(job_search_window, text="Apply", command=apply_job).pack(pady=10)

    # creating back button
    backicon=tk.PhotoImage(file='icons/back.png')
    backbtn=tk.Button(job_search_window,image=backicon,bd=0,cursor='hand2',fg="black",bg="white",command=backhomepage)
    backbtn.place(x=10,y=370)

    job_search_window.mainloop()

# Function to search jobs
def search_jobs():
    title = title_var.get().strip()
    location = location_var.get().strip()
    salary = salary_var.get().strip()

    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    query = "SELECT id, job_title, location, salary FROM jobs WHERE 1=1"
    params = []

    if title:
        query += " AND job_title LIKE %s"
        params.append(f"%{title}%")
    if location:
        query += " AND location LIKE %s"
        params.append(f"%{location}%")
    if salary:
        query += " AND salary >= %s"
        params.append(salary)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    for item in job_list.get_children():
        job_list.delete(item)

    if results:
        for row in results:
            job_list.insert("", "end", values=row)
    else:
        messagebox.showinfo("No Results", "No matching jobs found.")

# Function to apply for a job
def apply_job():
    if logged_in_user_id is None:
        messagebox.showerror("Login Required", "Please log in to apply for jobs.")
        return

    selected_item = job_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a job to apply.")
        return

    job_id = job_list.item(selected_item, "values")[0]
    
    try:
        job_id = int(job_id)
    except ValueError:
        messagebox.showerror("Error", "Invalid job ID format.")
        return

    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications WHERE job_id = %s AND users = %s", (job_id, logged_in_user_id))
    existing_application = cursor.fetchone()

    if existing_application:
        messagebox.showinfo("Application Error", "You have already applied for this job.")
    else:
        query = "INSERT INTO applications (job_id, users, status) VALUES (%s, %s, 'pending')"
        cursor.execute(query, (job_id, logged_in_user_id))
        conn.commit()
        messagebox.showinfo("Application Submitted", "You have successfully applied for the job.")

    conn.close()

# Open job search page without login
open_job_search_page()
