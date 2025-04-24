import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import os

# Connect to MySQL Database
def connect_db():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="jobmatrix")
        return conn
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# Replace this with the actual logged-in user ID after login
logged_in_user_id =1   # Change dynamically based on login session

# Function to fetch applied jobs
def fetch_applied_jobs():
    if logged_in_user_id is None:
        messagebox.showerror("Error", "User not logged in!")
        return

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT a.id, j.job_title, j.company, j.location, j.salary, a.status
            FROM applications a
            JOIN jobs j ON a.job_id = j.id
            WHERE a.users = %s
        """
        cursor.execute(query, (logged_in_user_id,))
        results = cursor.fetchall()
        
        # Clear previous results
        job_list.delete(*job_list.get_children())

        # Insert fetched results into table
        if results:
            for row in results:
                job_list.insert("", "end", values=row)
        else:
            messagebox.showinfo("No Jobs", "You have not applied for any jobs.")
    
    except pymysql.Error as e:
        messagebox.showerror("Query Error", f"Error: {e}")
    
    finally:
        conn.close()

# Function to cancel job application
def cancel_application():
    selected_item = job_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a job to cancel.")
        return
    
    app_id = job_list.item(selected_item[0], "values")[0]  # Get application ID
    
    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        query = "DELETE FROM applications WHERE id = %s"
        cursor.execute(query, (app_id,))
        conn.commit()
        messagebox.showinfo("Success", "Your job application has been canceled.")
        fetch_applied_jobs()  # Refresh the job list after canceling

    except pymysql.Error as e:
        messagebox.showerror("Query Error", f"Error: {e}")
    
    finally:
        conn.close()

# Function to go back to home page
def backhomepage():
    view_jobs_window.destroy()
    import UserHome  # Ensure this module exists

# Initialize Tkinter Window
view_jobs_window = tk.Tk()
view_jobs_window.title("View Applied Jobs")
view_jobs_window.geometry("800x400")
view_jobs_window.configure(bg="#f0f0f0")

# Table to display applied jobs
columns = ("App ID", "Job Title", "Company", "Location", "Salary", "Status")
job_list = ttk.Treeview(view_jobs_window, columns=columns, show="headings")

for col in columns:
    job_list.heading(col, text=col)
    job_list.column(col, width=130)
job_list.pack(fill="both", expand=True, padx=10, pady=10)

# Buttons
button_frame = tk.Frame(view_jobs_window, bg="#f0f0f0")
button_frame.pack(pady=10)

refresh_button = ttk.Button(button_frame, text="Refresh", command=fetch_applied_jobs)
refresh_button.grid(row=0, column=0, padx=10)

cancel_button = ttk.Button(button_frame, text="Cancel Job", command=cancel_application)
cancel_button.grid(row=0, column=1, padx=10)

# Load back button image safely
back_icon_path = "icons/back.png"  # Ensure this path is correct
if os.path.exists(back_icon_path):
    back_icon = tk.PhotoImage(file=back_icon_path)
    backbtn = tk.Button(view_jobs_window, image=back_icon, bd=0, cursor="hand2", bg="#f0f0f0", command=backhomepage)
    backbtn.image = back_icon  # Prevent garbage collection
    backbtn.place(x=10, y=350)
else:
    backbtn = ttk.Button(view_jobs_window, text="Back", command=backhomepage)
    backbtn.pack(pady=5)

# Fetch applied jobs when the window opens
fetch_applied_jobs()

view_jobs_window.mainloop()
