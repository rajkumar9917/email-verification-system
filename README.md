# 📧 Django Email Verification & Bulk Email System

A full-stack Django project that allows users to **send emails, verify email addresses, and send bulk emails using CSV upload**.  

---

## 🚀 Features

### ✉️ Email System
- Send single emails using Gmail SMTP
- Secure email configuration using `.env`
- Email logging system
- Admin panel integration

### 📤 Bulk Email Sender
- Upload CSV file with multiple email addresses
- Send bulk emails in one click
- Success / failure tracking
- Email logs saved in database

### ✅ Email Verifier
- Email format validation
- Domain verification
- Invalid email detection

### 🔐 Security
- Environment variables used for SMTP credentials
- `.gitignore` configured to protect sensitive data

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Email Service:** Gmail SMTP


---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/email-verification-system.git
cd email-verification-system

```
---

## Create Virtual Environment

python -m venv .venv  
for window - .venv\Scripts\activate

---

## Install dependencies

pip install -r requirements.txt

---
## Create .env file
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

## Run migrations
python manage.py makemigrations  
python manage.py migrate

---

## Run Server
python manage.py runserver


http://127.0.0.1:8000/

---

## Create Super User
python manage.py createsuperuser


http://127.0.0.1:8000/admin/
---