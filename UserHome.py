# from tkinter import *
# from PIL import ImageTk  # PIL for image handling
# import pymysql  # MySQL library
# from tkinter import messagebox


# # Global variable to store logged-in user ID
# logged_in_user_id = None  

# def set_user_id(user_id):
#     """Store the logged-in user ID globally."""
#     global logged_in_user_id
#     logged_in_user_id = user_id
#     print(f"User ID set in Home: {logged_in_user_id}")  # Debugging

# def logout():
#     # """Logout and return to login screen."""
#     root.destroy()
#     import userSignIn

# def search_jobs():
#     # """Open the job search page with the logged-in user ID."""
#     # if logged_in_user_id is None:
#     #     messagebox.showerror("Error", "User ID not found! Please log in again.")
#     # else:
#     root.destroy()
#     import userSearch
#     # userSearch.open_search_page(logged_in_user_id)

# def view_applied_jobs():
#     # """Open the applied jobs page with the logged-in user ID."""
#     # if logged_in_user_id is None:
#     #     messagebox.showerror("Error", "User ID not found! Please log in again.")
#     # else:
#         root.destroy()
#         import userViewAppliedJobs
#         # userViewAppliedJobs.open_applied_jobs_page(logged_in_user_id)

# def settings():
    
#     print("Settings Clicked")

# def show_menu():
#     # """Toggle the sidebar menu."""
#     if menu_frame.winfo_ismapped():
#         menu_frame.place_forget()  # Hide the menu if visible
#     else:
#         menu_frame.place(x=10, y=180)  # Show menu

# # Initialize main window
# root = Tk()
# root.geometry('861x461+50+50')
# root.title("User Home")

# # Load background image
# bg1 = ImageTk.PhotoImage(file="images/userhome.png")
# bglabel = Label(root, image=bg1)
# bglabel.place(x=0, y=0)

# # Menu Button (☰)
# menu_button = Button(root, text="☰", font=("Arial", 14), command=show_menu, bg="white", fg="black", bd=0)
# menu_button.place(x=10, y=140)

# # Menu Frame (Initially Hidden)
# menu_frame = Frame(root, bg="blue", relief="raised", bd=2)

# # Menu Buttons
# Button(menu_frame, text="Search Jobs", command=search_jobs, width=20, bg="white").pack(pady=5)
# Button(menu_frame, text="View Applied Jobs", command=view_applied_jobs, width=20, bg="white").pack(pady=5)
# Button(menu_frame, text="Settings", command=settings, width=20, bg="white").pack(pady=5)

# # Logout Button
# logout_btn = Button(root, text='Logout', font=('Segoe UI Symbol', 10, 'bold'), fg='red', cursor='hand2', bd=0, command=logout)
# logout_btn.place(x=700, y=10, height=30, width=100)

# # Logout Icon
# logout_icon = PhotoImage(file='icons/logout.png')
# logout_icon_btn = Button(root, image=logout_icon, bd=0, cursor='hand2', command=logout)
# logout_icon_btn.place(x=790, y=10, height=30)

# root.mainloop()

from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import filedialog, messagebox
import os

# Global variable to store logged-in user ID
logged_in_user_id = 1  

def set_user_id(user_id):
    """Store the logged-in user ID globally."""
    global logged_in_user_id
    logged_in_user_id = user_id
    print(f"User ID set in Home: {logged_in_user_id}")  # Debugging

def logout():
    """Logout and return to login screen."""
    root.destroy()
    import userSignIn

def search_jobs():
    """Open the job search page."""
    root.destroy()
    import userSearch

def view_applied_jobs():
    """Open the applied jobs page."""
    root.destroy()
    import userViewAppliedJobs

def settings():
    print("Settings Clicked")

def show_menu():
    """Toggle the sidebar menu."""
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()  # Hide the menu if visible
    else:
        menu_frame.place(x=10, y=180)  # Show menu

def upload_resume():
    """Allow the user to upload a resume and save the file path in the database."""
    if logged_in_user_id is None:
        messagebox.showerror("Error", "User ID not found! Please log in again.")
        return
    
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
    
    if file_path:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="123456", database="jobmatrix")
            cursor = conn.cursor()
            cursor.execute("UPDATE User SET resume_path = %s WHERE id = %s", (file_path, logged_in_user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Resume uploaded successfully!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error saving resume: {e}")
    else:
        messagebox.showerror("File Error", "No file selected")

def view_resume():
    """Fetch and open the user's uploaded resume."""
    if logged_in_user_id is None:
        messagebox.showerror("Error", "User ID not found! Please log in again.")
        return
    
    try:
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="jobmatrix")
        cursor = conn.cursor()
        cursor.execute("SELECT resume_path FROM User WHERE id = %s", (logged_in_user_id,))
        result = cursor.fetchone()
        conn.close()

        if result and result[0]:
            resume_path = result[0]
            if os.path.exists(resume_path):
                os.startfile(resume_path)  # Opens the file
            else:
                messagebox.showerror("File Not Found", "Resume file not found on your system.")
        else:
            messagebox.showerror("No Resume", "You have not uploaded a resume yet.")
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error fetching resume: {e}")

# Initialize main window
root = Tk()
root.geometry('861x461+50+50')
root.title("User Home")

# Load background image
bg1 = ImageTk.PhotoImage(file="images/userhome.png")
bglabel = Label(root, image=bg1)
bglabel.place(x=0, y=0)

# Menu Button (☰)
menu_button = Button(root, text="☰", font=("Arial", 14), command=show_menu, bg="white", fg="black", bd=0)
menu_button.place(x=10, y=140)

# Menu Frame (Initially Hidden)
menu_frame = Frame(root, bg="blue", relief="raised", bd=2)

# Menu Buttons
Button(menu_frame, text="Search Jobs", command=search_jobs, width=20, bg="white").pack(pady=5)
Button(menu_frame, text="View Applied Jobs", command=view_applied_jobs, width=20, bg="white").pack(pady=5)
Button(menu_frame, text="Upload Resume", command=upload_resume, width=20, bg="white").pack(pady=5)
Button(menu_frame, text="View Resume", command=view_resume, width=20, bg="white").pack(pady=5)  # New Button
Button(menu_frame, text="Settings", command=settings, width=20, bg="white").pack(pady=5)

# Logout Button
logout_btn = Button(root, text='Logout', font=('Segoe UI Symbol', 10, 'bold'), fg='red', cursor='hand2', bd=0, command=logout)
logout_btn.place(x=700, y=10, height=30, width=100)

# Logout Icon
logout_icon = PhotoImage(file='icons/logout.png')
logout_icon_btn = Button(root, image=logout_icon, bd=0, cursor='hand2', command=logout)
logout_icon_btn.place(x=790, y=10, height=30)

root.mainloop()
