User Registration Django Project

📌 Overview

This is a User Registration system built with Django. The project allows users to sign up, log in, log out, and reset their passwords. It also includes features like email verification and OTP-based password recovery.

This project is ideal for learning Django, user authentication, and integrating email services like Mailgun for transactional emails.

🛠 Features

- User Signup & Login – Secure registration and authentication.

- Email Verification – Verify user email upon registration.

- Password Reset via OTP – Users can reset their passwords securely.

- Profile Management – Users can manage their personal information (optional).

- Secure Passwords – Passwords are hashed using Django’s built-in authentication system.

⚙️ Technologies Used

- Python 

- Django 

- SQLite (default)

- HTML / CSS (for frontend templates)

💻 Installation

1. Clone the repository

        git clone https://github.com/yourusername/user-registration.git
        cd user-registration

2. Create a virtual environment

        python -m venv env
        source env/bin/activate  # Linux / Mac
        env\Scripts\activate     # Windows

3. Install dependencies

        pip install -r requirements.txt

4. Apply migrations

        python manage.py migrate

5. Create a superuser (optional, for admin access)

        python manage.py createsuperuser

6. Run the server

        python manage.py runserver

- Visit http://127.0.0.1:8000/ in your browser.
