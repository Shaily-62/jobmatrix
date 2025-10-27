💼 Job Portal Application (Python + Tkinter + MySQL)

This is a desktop-based Job Portal Application built using Python (Tkinter) for the graphical user interface and MySQL for the database.
It provides an easy way for job seekers to find and apply for jobs, and for employers to post and manage job listings — all in one platform.

🎯 Project Overview

The main goal of this project is to create an end-to-end job management system that connects employers and job seekers.
Both users and employers can log in, perform their respective operations, and interact through the database in real time.

🧑‍💻 Tech Stack
Category - Technology
Programming Language	- Python
GUI Framework	- Tkinter
Database -	MySQL
Connector	- mysql.connector
IDE Used - 	VS Code

🗂️ Project Structure
├── icons/                     # Icons used in the interface
├── images/                    # Images used in the application
├── EmpManageJobs.py           # Employer: Manage job listings
├── EmpViewJob.py              # Employer: View job details
├── empPostJob.py              # Employer: Post new jobs
├── empManageCandidates.py     # Employer: View candidate applications
├── empHome.py                 # Employer dashboard
├── empsignin.py               # Employer login
├── empsignup.py               # Employer registration
├── UserHome.py                # User dashboard
├── UserSignUp.py              # User registration
├── userSignIn.py              # User login
├── userSearch.py              # Job search window
├── userViewAppliedJobs.py     # View applied jobs
├── welcome.py                 # Main entry point
├── .gitignore
└── __pycache__/               # Cached files

🧩 Key Features
👤 User Side

Register and log in

Search for jobs

Apply for job postings

View applied jobs

🏢 Employer Side

Sign up and log in

Post new jobs

Manage job listings

View candidates who applied

📊 Database Overview
Table -	Purpose
users	 - Stores user details
employers	- Stores employer details
jobs	- Contains job listings
applications	- Tracks which user applied to which job
