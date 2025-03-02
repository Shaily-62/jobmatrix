import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk

# Global variable to store logged-in user ID
logged_in_user_id = None

# Connect to MySQL database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="jobmatrix"
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# Function to authenticate user
def login():
    global logged_in_user_id
    email = email_var.get().strip()
    password = password_var.get().strip()
    
    conn = connect_db()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM User WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        logged_in_user_id = user[0]
        login_window.destroy()
        root.deiconify()  # Show job search window
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

# Function to search jobs by title, location, and salary
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

# Function to apply for a selected job
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

# Function to go back to homepage
def backHomepage():
    root.destroy()
    import UserHome

# Create login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Email:").pack(pady=5)
email_var = tk.StringVar()
tk.Entry(login_window, textvariable=email_var).pack(pady=5)

tk.Label(login_window, text="Password:").pack(pady=5)
password_var = tk.StringVar()
tk.Entry(login_window, textvariable=password_var, show="*").pack(pady=5)

tk.Button(login_window, text="Login", command=login).pack(pady=10)

# Hide main window until login
root = tk.Tk()
root.withdraw()
root.title("Job Search")
root.geometry("800x400")
root.configure(bg="#f0f0f0")

title_var = tk.StringVar()
location_var = tk.StringVar()
salary_var = tk.StringVar()

frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Job Title:").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(frame, textvariable=title_var).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Location:").grid(row=0, column=2, padx=5, pady=5)
ttk.Entry(frame, textvariable=location_var).grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame, text="Min Salary:").grid(row=0, column=4, padx=5, pady=5)
ttk.Entry(frame, textvariable=salary_var).grid(row=0, column=5, padx=5, pady=5)

ttk.Button(frame, text="Search", command=search_jobs).grid(row=0, column=6, padx=5, pady=5)

# backicon = tk.PhotoImage(file='icons/back.png')
backbtn = ttk.Button(root, text="Back", cursor='hand2', command=backHomepage)
backbtn.place(x=700, y=15)

columns = ("Job ID", "Job Title", "Location", "Salary")
job_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    job_list.heading(col, text=col)
    job_list.column(col, width=150)
job_list.pack(fill="both", expand=True)

apply_button = ttk.Button(root, text="Apply", command=apply_job)
apply_button.pack(pady=10)

login_window.mainloop()
root.mainloop()