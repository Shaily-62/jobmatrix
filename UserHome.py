from tkinter import*
from PIL import ImageTk     #pil python image lib
import pymysql                #pip install pymysql
from tkinter import messagebox


def Logout():
    root.destroy()
    import userSignIn


def search_jobs():
   root.destroy()
   import userSearch

def view_applied_jobs():
    print("View Applied Jobs Clicked")

def setting():
    print("Setting Clicked")


def show_menu():
    """Function to toggle the sidebar menu"""
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()  # Hide the menu if it's visible
    else:
        menu_frame.place(x=10, y=180)  # Show the menu below ☰ button

root = Tk()
root.geometry('861x461+50+50')
root.title("UserSignIn")  # Corrected the title setting

# Load background image
bg1 = ImageTk.PhotoImage(file="images/userhome.png")
bglabel = Label(root, image=bg1)
bglabel.place(x=0, y=0)

# Create a Menu Button (☰)
menu_button = Button(root, text="☰", font=("Arial", 14), command=show_menu, bg="white", fg="black", bd=0)
menu_button.place(x=10, y=140)  # Position at top-left corner

# Create a Menu Frame (Initially Hidden)
menu_frame = Frame(root, bg="blue", relief="raised", bd=2)

# Add Menu Buttons inside Frame
Button(menu_frame, text="Search Jobs", command=search_jobs, width=20, bg="white").pack(pady=5)
Button(menu_frame, text="View Applied Jobs", command=view_applied_jobs, width=20, bg="white").pack(pady=5)
Button(menu_frame, text="Setting", command=setting, width=20, bg="white").pack(pady=5)

# Logout Button
logout = Button(root, text='Logout', font=('Segoe UI Symbol', 10, 'bold'), fg='red', cursor='hand2', bd=0, command=Logout)
logout.place(x=700, y=10, height=30, width=100)

# Logout Icon Button
logouticon = PhotoImage(file='icons/logout.png')
logoutbtn = Button(root, image=logouticon, bd=0, cursor='hand2', command=Logout)
logoutbtn.place(x=790, y=10, height=30)

root.mainloop()
