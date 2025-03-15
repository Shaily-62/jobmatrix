from tkinter import *
from PIL import ImageTk  # PIL for image handling
import pymysql  # MySQL library
from tkinter import messagebox


# Global variable to store logged-in user ID
logged_in_user_id = None  

def set_user_id(user_id):
    """Store the logged-in user ID globally."""
    global logged_in_user_id
    logged_in_user_id = user_id
    print(f"User ID set in Home: {logged_in_user_id}")  # Debugging

def logout():
    # """Logout and return to login screen."""
    root.destroy()
    import userSignIn

def search_jobs():
    # """Open the job search page with the logged-in user ID."""
    # if logged_in_user_id is None:
    #     messagebox.showerror("Error", "User ID not found! Please log in again.")
    # else:
    root.destroy()
    import userSearch
    # userSearch.open_search_page(logged_in_user_id)

def view_applied_jobs():
    # """Open the applied jobs page with the logged-in user ID."""
    # if logged_in_user_id is None:
    #     messagebox.showerror("Error", "User ID not found! Please log in again.")
    # else:
        root.destroy()
        import userViewAppliedJobs
        # userViewAppliedJobs.open_applied_jobs_page(logged_in_user_id)

def settings():
    
    print("Settings Clicked")

def show_menu():
    # """Toggle the sidebar menu."""
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()  # Hide the menu if visible
    else:
        menu_frame.place(x=10, y=180)  # Show menu

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
Button(menu_frame, text="Settings", command=settings, width=20, bg="white").pack(pady=5)

# Logout Button
logout_btn = Button(root, text='Logout', font=('Segoe UI Symbol', 10, 'bold'), fg='red', cursor='hand2', bd=0, command=logout)
logout_btn.place(x=700, y=10, height=30, width=100)

# Logout Icon
logout_icon = PhotoImage(file='icons/logout.png')
logout_icon_btn = Button(root, image=logout_icon, bd=0, cursor='hand2', command=logout)
logout_icon_btn.place(x=790, y=10, height=30)

root.mainloop()
