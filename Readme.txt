# Sheikh Rafiq Computers — Company Management Portal

> A secure, role-based web application for managing company data, IT operations, and business workflows — built and deployed at [srm.srcomputer.net](https://srm.srcomputer.net)

---

## Overview

This is a full-stack internal management system developed for **Sheikh Rafiq Computers**, a UAE-based IT support and computer services company. The platform centralises company records, user access control, and operational data into one secure, auditable system.

The project was designed with security as a core requirement — not an afterthought — implementing industry-standard cryptographic practices and access control patterns throughout.

---

## Live Demo

**[https://srm.srcomputer.net](https://srm.srcomputer.net)**

| Role | Login URL |
|------|-----------|
| Admin | [/login](https://srm.srcomputer.net/login) |
| User | [/user-login](https://srm.srcomputer.net/user-login) |

---

## Features

### Security
- **SHA-256 password hashing** with unique salting per user — plaintext passwords are never stored
- **Session-based authentication** with secure, signed cookies
- **Role-based access control (RBAC)** — strict separation between Admin and User permissions
- **Audit logs** — every significant action is logged with timestamp and user identity
- **OTP authentication** support for enhanced login security

### Admin Dashboard
- Manage company records, user accounts, and operational data
- View full audit trail of system activity
- Create, read, update, and delete company information

### User Dashboard
- Scoped access — users only see and interact with what they are permitted to
- Clean interface for accessing assigned content and workflow pages

### General
- Responsive frontend design (works on desktop and mobile)
- Organised, professional layout for daily business use

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite3 |
| Cryptography | SHA-256, Salting, Fernet Encryption |
| Auth | Session cookies, OTP |
| Deployment | Live at srm.srcomputer.net |

---

## Security Implementation Details

This project was built as part of a cybersecurity-focused development approach:

- **Password Storage:** Passwords are hashed using SHA-256 with a randomly generated salt per user. This protects against rainbow table attacks.
- **Session Management:** Flask sessions use signed cookies to prevent tampering.
- **Access Control:** Every route checks the users role before rendering. Unauthorised access attempts are blocked and logged.
- **Audit Logging:** Admin actions (login, record changes, user management) are written to an audit log table with timestamps.
- **Encryption:** Sensitive data fields use Fernet symmetric encryption before being stored in the database.

---

## Project Structure

```
srm/
├── app.py               # Main Flask application & route definitions
├── database.py          # Database setup and helper functions
├── auth.py              # Authentication logic (hashing, sessions, OTP)
├── templates/
│   ├── index.html       # Landing page
│   ├── login.html       # Admin login
│   ├── user_login.html  # User login
│   ├── admin/           # Admin dashboard templates
│   └── user/            # User dashboard templates
├── static/
│   ├── logo.png
│   └── style.css
└── README.md
```

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Saudshk/Srm.git
cd Srm

# 2. Install dependencies
pip install flask cryptography

# 3. Initialise the database
python database.py

# 4. Run the application
python app.py
```

The app will run at `http://localhost:5000` by default.

---

## What I Learned

Building this project reinforced several real-world security and development concepts:

- Proper credential storage using hashing + salting (vs. storing plaintext or using weak MD5/SHA-1)
- Designing RBAC systems from scratch — understanding how privilege separation prevents unauthorised access
- The importance of audit logging for accountability and incident response
- Deploying a Flask application to a live production environment

---

## Author

**Saud Ahmed Mukhtar Ahmed Shaikh**  
BSc Cybersecurity — University of West London  
CEH (In Progress) | Advanced Pentesting — RedTeam Academy  
[LinkedIn](https://www.linkedin.com/in/saud-mukhtar-shaikh-039b3330b/) | [GitHub](https://github.com/Saudshk)

---

> *Built as part of an IT internship at Sheikh Rafiq Computers, Sharjah, UAE.*
