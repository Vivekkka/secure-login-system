## Secure Login System with Role-Based Access Control
## Project Overview

This project is a secure web-based login system developed as part of my Cyber Security Internship.
It implements authentication, authorization, and multiple security controls to protect against common web attacks.

The system supports User and Admin roles with restricted access and includes protections such as password hashing, account lockout, and input validation.

## Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS

Database: SQLite

Security: bcrypt, Flask sessions

Tools: VS Code, GitHub

## Setup Instructions
## 1️ Clone the Repository
git clone <your-github-repo-link>
cd secure-login-system

## 2️ Install Dependencies
pip install flask flask-sqlalchemy flask-bcrypt

## 3️ Run the Application
python app.py

## 4️ Open in Browser
http://127.0.0.1:5000

## Features Implemented
## User Registration

New users can register with username, email, password, and role

Duplicate email registration is prevented

Passwords are securely hashed using bcrypt

## User Login

Secure login with email and password

Session-based authentication

Role-based redirection after login

## Role-Based Access Control (RBAC)

Admin: Can view all registered users

User: Can access only user dashboard

Unauthorized access is restricted

## Security Enhancements

Input validation to prevent SQL Injection

Password hashing using bcrypt

Account lockout after multiple failed login attempts

Session protection after logout

## Testing Performed

Successful registration and login

Duplicate email registration check

Invalid credentials handling

Account lockout after 3 failed login attempts

Session protection after logout

Database verification for hashed passwords

## Screenshots (System in Action)

VS Code project structure

Registration page

Registration success message

Login page

Successful login redirect

Admin dashboard (user list)

Account lockout message

SQLite database structure

## Challenges Faced & Solutions
## Issue: Duplicate Registration

Problem: Users could register with the same email

Solution: Implemented unique email validation using database queries

## Issue: Password Security

Problem: Plain-text passwords are insecure

Solution: Implemented bcrypt password hashing

## Issue: Brute Force Login Attempts

Problem: Unlimited login attempts

Solution: Implemented failed login counter and account lockout mechanism

## Issue: Unauthorized Access

Problem: Users accessing admin routes

Solution: Implemented role-based access control using Flask sessions

## Conclusion

This project helped me gain hands-on experience in building a secure authentication system while applying cybersecurity principles such as access control, secure password storage, and attack prevention mechanisms.

## Author

Vivek Kumar Digar
Cyber Security Intern