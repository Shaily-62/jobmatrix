import tkinter as tk
from tkinter import ttk, messagebox
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
root.title("Job Management System")
root.geometry('1000x600+50+50')
root.configure(bg="#f0f4f7")

def fetch_jobs():
    cursor.execute("SELECT id, job_title, company, description, salary, location FROM jobs")
    rows = cursor.fetchall()
    for row in job_table.get_children():
        job_table.delete(row)
    for row in rows:
        job_table.insert("", "end", values=row)

def clear_fields():
    title_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    desc_entry.delete("1.0", tk.END)
    salary_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    update_btn.config(state="disabled")
    delete_btn.config(state="disabled")

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
        update_btn.config(state="normal")
        delete_btn.config(state="normal")

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
        query = """
            UPDATE jobs 
            SET job_title=%s, company=%s, description=%s, salary=%s, location=%s 
            WHERE id=%s
        """
        values = (
            title_entry.get(),
            company_entry.get(),
            desc_entry.get("1.0", tk.END).strip(),
            salary_entry.get(),
            location_entry.get(),
            job_id
        )
        cursor.execute(query, values)
        conn.commit()
        fetch_jobs()
        messagebox.showinfo("Success", "Job updated successfully")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Update failed: {str(e)}")

def delete_job():
    selected = job_table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a job to delete")
        return

    job_id = job_table.item(selected)['values'][0]
    job_title = job_table.item(selected)['values'][1]

    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the job: '{job_title}'?")
    if confirm:
        try:
            cursor.execute("DELETE FROM jobs WHERE id=%s", (job_id,))
            conn.commit()
            fetch_jobs()
            messagebox.showinfo("Success", "Job deleted successfully")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete job: {str(e)}")


# Entry Frame
frame = tk.LabelFrame(root, text="Job Details", font=("Segoe UI", 12, "bold"), bg="#ffffff", padx=20, pady=10)
frame.pack(pady=20)

labels = ["Job Title", "Company", "Description", "Salary", "Location"]
title_entry = tk.Entry(frame, font=("Segoe UI", 10))
company_entry = tk.Entry(frame, font=("Segoe UI", 10))
desc_entry = tk.Text(frame, height=3, width=30, font=("Segoe UI", 10))
salary_entry = tk.Entry(frame, font=("Segoe UI", 10))
location_entry = tk.Entry(frame, font=("Segoe UI", 10))
inputs = [title_entry, company_entry, desc_entry, salary_entry, location_entry]

for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Segoe UI", 10, "bold"), bg="#ffffff").grid(row=i, column=0, sticky="w", pady=3)
    if isinstance(inputs[i], tk.Text):
        inputs[i].grid(row=i, column=1, pady=3, padx=5)
    else:
        inputs[i].grid(row=i, column=1, sticky="ew", pady=3, padx=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

style_btn = {"font": ("Segoe UI", 10, "bold"), "bg": "#4CAF50", "fg": "white", "width": 15, "bd": 0, "cursor": "hand2"}

tk.Button(btn_frame, text="Add Job", command=add_job, **style_btn).grid(row=0, column=0, padx=10)
update_btn = tk.Button(btn_frame, text="Update Job", command=update_job, state="disabled", **style_btn)
update_btn.grid(row=0, column=1, padx=10)
delete_btn = tk.Button(btn_frame, text="Delete Job", command=delete_job, state="disabled", **style_btn)
delete_btn.grid(row=0, column=2, padx=10)

# Treeview (Job Table)
table_frame = tk.Frame(root)
table_frame.pack(pady=20, fill="both", expand=True)

scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
scroll_y = tk.Scrollbar(table_frame, orient="vertical")

columns = ("ID", "Job Title", "Company", "Description", "Salary", "Location")
job_table = ttk.Treeview(table_frame, columns=columns, show="headings", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side="bottom", fill="x")
scroll_y.pack(side="right", fill="y")
scroll_x.config(command=job_table.xview)
scroll_y.config(command=job_table.yview)

for col in columns:
    job_table.heading(col, text=col)
    job_table.column(col, width=140, anchor="center")

job_table.pack(fill="both", expand=True)
job_table.bind("<ButtonRelease-1>", populate_fields)

# Back Button
backicon = tk.PhotoImage(file='icons/back.png')
backbtn = tk.Button(root, image=backicon, bd=0, cursor='hand2', bg="#f0f4f7", command=backHomepage)
backbtn.place(x=10, y=10)

fetch_jobs()

root.mainloop()
conn.close()
