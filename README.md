# Django Login System with PostgreSQL

A basic but functional user authentication system built using **Django**, integrated with **PostgreSQL**. This project implements a login, registration, and logout system using Django’s built-in authentication features, custom user forms, and static frontend templates styled with HTML, CSS, and JavaScript.

> ✅ The system currently supports full user registration and login functionality. All connections to the database are working, and the project is fully ready for extension or deployment.

---

## 🚀 Features

- User Registration with custom form
- User Login & Logout
- PostgreSQL integration
- Django Templates for frontend
- HTML + CSS + JavaScript for styling
- Static files served properly
- Environment separation (Development / Production)
- Virtual environments usage
- Variables controlled via `DJANGO_PRODUCTION` flag
- Two requirements files:  
  - `desarrollo.txt`  
  - `produccion.txt`

---

## 🧰 Technologies Used

- **Django 4**
- **PostgreSQL**
- **HTML / CSS / JavaScript**
- **Gunicorn + mod_wsgi** (for production)
- **django-environ**, **whitenoise**, etc.
- Linux + virtualenv
- Systemd services (e.g. `pgadmin4.service`)

---
## 🔧 Setup Instructions

1. Clone the repository
    https://github.com/Hakiller777/Proyecto-1.git

2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install Dependencies

For development:

pip install -r desarrollo.txt

For production:

pip install -r produccion.txt

4. Set Environment Variable

In your terminal:

export DJANGO_PRODUCTION=false  # for development

Or in .env file:

DJANGO_PRODUCTION=false

5. Run the App

python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.

6. Deployment Notes

Production server can use Gunicorn or mod_wsgi with Apache.

You may use systemctl for services like pgAdmin.

Configure static files with whitenoise or Apache/NGINX.

PostgreSQL database is already connected and tested.



