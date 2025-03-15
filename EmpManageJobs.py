import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

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
root.title("Job Management System")
root.geometry('861x461+50+50')

def fetch_jobs():
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    for row in job_table.get_children():
        job_table.delete(row)
    for row in rows:
        job_table.insert("", "end", values=row)

def populate_fields(event):
    selected = job_table.focus()
    if not selected:
        return
    values = job_table.item(selected, 'values')
    if values:
        title_entry.delete(0, tk.END)
        title_entry.insert(0, values[1])
        company_entry.delete(0, tk.END)
        company_entry.insert(0, values[2])
        desc_entry.delete("1.0", tk.END)
        desc_entry.insert("1.0", values[3].strip())
        salary_entry.delete(0, tk.END)
        salary_entry.insert(0, values[4])
        location_entry.delete(0, tk.END)
        location_entry.insert(0, values[5])
        emp_id_entry.delete(0, tk.END)
        emp_id_entry.insert(0, str(values[6]))

def add_job():
    root.destroy()
    import empPostJob

def update_job():
    selected = job_table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a job to update")
        return
    job_id = job_table.item(selected)['values'][0]
    try:
        emp_id = int(emp_id_entry.get()) if emp_id_entry.get().isdigit() else None
        query = "UPDATE jobs SET job_title=%s, company=%s, description=%s, salary=%s, location=%s, emp_id=%s WHERE id=%s"
        values = (title_entry.get(), company_entry.get(), desc_entry.get("1.0", tk.END).strip(), salary_entry.get(), location_entry.get(), emp_id, job_id)
        cursor.execute(query, values)
        conn.commit()
        fetch_jobs()
        messagebox.showinfo("Success", "Job updated successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed: {str(e)}")

def delete_job():
    selected = job_table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a job to delete")
        return
    job_id = job_table.item(selected)['values'][0]
    cursor.execute("DELETE FROM jobs WHERE id=%s", (job_id,))
    conn.commit()
    fetch_jobs()
    messagebox.showinfo("Success", "Job deleted successfully")

# UI Components
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Job Title").grid(row=0, column=0)
title_entry = tk.Entry(frame)
title_entry.grid(row=0, column=1)

tk.Label(frame, text="Company").grid(row=1, column=0)
company_entry = tk.Entry(frame)
company_entry.grid(row=1, column=1)

tk.Label(frame, text="Description").grid(row=2, column=0)
desc_entry = tk.Text(frame, height=3, width=30)
desc_entry.grid(row=2, column=1)

tk.Label(frame, text="Salary").grid(row=3, column=0)
salary_entry = tk.Entry(frame)
salary_entry.grid(row=3, column=1)

tk.Label(frame, text="Location").grid(row=4, column=0)
location_entry = tk.Entry(frame)
location_entry.grid(row=4, column=1)

tk.Label(frame, text="Employer ID").grid(row=5, column=0)
emp_id_entry = tk.Entry(frame)
emp_id_entry.grid(row=5, column=1)

# Buttons
tk.Button(frame, text="Add Job", command=add_job).grid(row=6, column=0, columnspan=2)
tk.Button(frame, text="Update Job", command=update_job).grid(row=7, column=0, columnspan=2)
tk.Button(frame, text="Delete Job", command=delete_job).grid(row=8, column=0, columnspan=2)

# Job Table
columns = ("ID", "Job Title", "Company", "Description", "Salary", "Location", "Employer ID")
job_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    job_table.heading(col, text=col)
    job_table.column(col, width=100)
job_table.pack(pady=10)

# Bind select event
job_table.bind("<ButtonRelease-1>", populate_fields)

fetch_jobs()
root.mainloop()

# Close database connection on exit
conn.close()
