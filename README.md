# 📧 Django Email Verification & Bulk Email System

A full-stack Django project that allows users to **send emails, verify email addresses, and send bulk emails using CSV upload**.

This project demonstrates how to build a **production-style email system in Django** with secure environment variables and bulk email functionality.

---

# 🚀 Features

## ✉️ Email System
- Send single emails using Gmail SMTP
- Secure email configuration using `.env`
- Email logging system
- Admin panel integration

## 📤 Bulk Email Sender
- Upload CSV file containing multiple email addresses
- Send bulk emails in one click
- Track success and failed emails
- Email logs saved in the database

## ✅ Email Verification
- Email format validation
- Domain verification
- Invalid email detection

## 🔐 Security
- Environment variables used for SMTP credentials
- `.gitignore` configured to protect sensitive data
- No credentials stored in source code

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|------|
| **Backend** | Django (Python) |
| **Database** | SQLite |
| **Frontend** | HTML, CSS |
| **Email Service** | Gmail SMTP |
| **Environment Variables** | python-dotenv |

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/rajkumar9917/email-verification-system.git
```

---

## 2️⃣ Navigate to Project Directory

```bash
cd email-verification-system
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / Mac**

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
```

⚠️ Use **Google App Password** instead of your Gmail password.

---

# 🗄 Database Setup

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# ▶️ Run Development Server

```bash
python manage.py runserver
```

Open in browser

```
http://127.0.0.1:8000/
```

---

# 👨‍💻 Create Admin User

```bash
python manage.py createsuperuser
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---