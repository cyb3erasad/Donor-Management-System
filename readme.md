# 🏥 Donor and Senior Citizen Management System (CareConnect)

A comprehensive web-based management system designed for NGOs to manage donations, donors, senior citizens, and special persons. Built with Flask, SQLAlchemy, and modern frontend technologies.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [User Roles](#user-roles)
- [Usage Guide](#usage-guide)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About the Project

**CareConnect** is a full-stack web application that helps NGOs and charitable organizations manage their donation programs efficiently. The system provides:

- **Transparent donation tracking** from donors to recipients
- **User management** for donors, senior citizens, and special persons
- **Financial oversight** with real-time balance tracking
- **Role-based dashboards** for different user types
- **Complete audit trail** of all transactions

### Problem It Solves

Many NGOs struggle with:
- ❌ Manual tracking of donations
- ❌ Lack of transparency in fund distribution
- ❌ Difficulty managing multiple beneficiary types
- ❌ No centralized system for donors and recipients

### Our Solution

✅ Automated donation management  
✅ Real-time financial tracking  
✅ Separate dashboards for each user type  
✅ Complete transparency with detailed history  
✅ Easy-to-use interface with modern design  

---

## ✨ Features

### For Donors
- 💳 **Make Donations** - Multiple payment methods (Easypaisa, Bank, PayPal, Cash)
- 📊 **Track Donations** - View complete donation history with dates and amounts
- 📈 **Dashboard Statistics** - See total contributions and impact

### For Senior Citizens & Special Persons
- 💰 **View Received Donations** - Complete history of financial support received
- 📅 **Track Support** - See dates, amounts, and purposes of each donation
- 📱 **Profile Management** - Maintain personal information
- 🏥 **Service Information** - Access to healthcare, food, education support details

### For Administrators
- 👥 **User Management** - Add/view/delete seniors, special people, and donors
- 💵 **Give Donations** - Distribute funds to beneficiaries with purpose tracking
- 📊 **Financial Dashboard** - Track total received, given, and remaining balance
- 📈 **Complete Statistics** - User counts, donation analytics, and more
- 🔍 **Full Transparency** - View all transactions with complete audit trail
- 📋 **Reports** - See who donated, who received, when, and why

---

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0** - Python web framework
- **SQLAlchemy 3.1.1** - ORM for database management
- **Flask-Login 0.6.3** - User session management
- **Werkzeug 3.0.1** - Password hashing and security

### Frontend
- **Jinja2** - Template engine
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - Client-side interactivity
- **HTML5** - Semantic markup

### Database
- **SQLite** - Lightweight database (development)
- Can be upgraded to **PostgreSQL** or **MySQL** for production

---

## 📁 Project Structure

```
donor-management-system/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── templates/                  # Jinja2 HTML templates
│   ├── base.html              # Base template with navbar/footer
│   ├── index.html             # Home page
│   ├── signin.html            # Sign in page
│   ├── signup.html            # Registration page
│   ├── donor_dashboard.html   # Donor dashboard
│   ├── senior_dashboard.html  # Senior citizen dashboard
│   └── admin_dashboard.html   # Admin control panel
│
├── static/                     # Static files (optional)
│   ├── css/                   # Custom CSS
│   ├── js/                    # Custom JavaScript
│   └── images/                # Images and assets
│
└── careconnect.db             # SQLite database (auto-created)
```

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.11 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads) (optional)

### Step-by-Step Installation

#### 1. Clone or Download the Project

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/donor-management-system.git
cd donor-management-system
```

**Option B: Download ZIP**
- Download the project ZIP file
- Extract it to your desired location
- Open terminal/command prompt in the extracted folder

#### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- Werkzeug 3.0.1

#### 4. Verify Installation

```bash
pip list
```

You should see all the packages listed above.

---

## ▶️ Running the Application

### First Time Setup

1. **Navigate to project directory:**
```bash
cd donor-management-system
```

2. **Activate virtual environment:**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Run the application:**
```bash
python app.py
```

4. **Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server.
Admin user created: admin@careconnect.org / admin123
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

5. **Open your browser and visit:**
```
http://127.0.0.1:5000
```

### Default Admin Credentials

When you run the application for the first time, a default admin account is created:

- **Email:** `admin@careconnect.org`
- **Password:** `admin123`

⚠️ **IMPORTANT:** Change this password after first login in production!

---

## 👥 User Roles

### 1. Admin
**Access Level:** Full system control

**Capabilities:**
- ✅ Add/delete senior citizens and special persons
- ✅ Add/delete donor information
- ✅ Give donations to beneficiaries
- ✅ View all users and transactions
- ✅ Track financial statistics
- ✅ Generate reports

**Dashboard Features:**
- Overview statistics
- User management
- Donation distribution
- Financial tracking

### 2. Donor
**Access Level:** Personal donation management

**Capabilities:**
- ✅ Make donations with multiple payment methods
- ✅ View donation history
- ✅ Track total contributions
- ✅ Update profile information

**Dashboard Features:**
- Total donations made
- Number of donations
- Last donation date
- Complete donation history

### 3. Senior Citizen / Special Person
**Access Level:** View received support

**Capabilities:**
- ✅ View received donations
- ✅ See donation purposes
- ✅ Track total support received
- ✅ Access service information

**Dashboard Features:**
- Profile information
- Total donations received
- Complete history of support
- Available services

---

## 📖 Usage Guide

### For New Users (Registration)

1. **Go to Sign Up Page**
   - Click "Sign Up" in the navigation bar

2. **Fill Registration Form**
   - Full Name
   - Email Address
   - Phone Number
   - Password (minimum 6 characters)
   - Select Category:
     - Donor (if you want to donate)
     - Senior Citizen (if you need support)
     - Special Person (if you need support)

3. **Submit and Sign In**
   - After registration, you'll be redirected to sign in
   - Use your email and password to log in

### For Donors

1. **Sign In**
   - Email: your@email.com
   - Password: yourpassword

2. **Make a Donation**
   - Click "Make a Donation" button
   - Fill in the form:
     - Your details (auto-filled)
     - CNIC Number
     - Donation Amount (minimum Rs 100)
     - Payment Method (Easypaisa/Bank/PayPal/Cash)
   - Submit

3. **View History**
   - Scroll down to see "Donation History"
   - View all your past donations with dates and amounts

### For Admin

1. **Sign In as Admin**
   - Email: admin@careconnect.org
   - Password: admin123

2. **Dashboard Overview**
   - See complete system statistics:
     - Total users count
     - Donations received from donors
     - Donations given to beneficiaries
     - **Remaining balance** (available funds)

3. **Add Users**
   - Click "Add Users" in sidebar
   - Choose "Senior Citizens" or "Special Peoples"
   - Fill the form:
     - Name, Email, Age, Contact Number
   - Submit

4. **Give Donations**
   - Click "Give Donations" in sidebar
   - See list of all senior citizens and special people
   - Click "Give" next to recipient
   - Fill donation form:
     - Amount
     - Purpose (Medical/Food/Education/Housing/Emergency/Monthly/Other)
     - Notes (optional)
   - Submit

5. **Track Finances**
   - Overview shows three key metrics:
     - 🟢 Total Received (from donors)
     - 🔴 Total Given (to beneficiaries)
     - 🔵 Remaining Balance (available funds)
   - View complete history of all transactions

### For Senior Citizens / Special Persons

1. **Sign In**
   - Use your registered email and password

2. **View Profile**
   - See your personal information
   - View member since date
   - **Total Received** amount displayed

3. **Check Received Donations**
   - Scroll to "Received Donations" section
   - View table with:
     - Date received
     - Amount
     - Purpose
     - Notes
     - Who gave it (Admin name)
     - Status

---

## 🗄️ Database Schema

### User Table
```python
- id (Primary Key)
- full_name (String)
- email (String, Unique)
- phone (String)
- password (Hashed)
- category (donor/senior/special/admin)
- registered_date (DateTime)
```

### SeniorCitizen Table (Admin-added)
```python
- id (Primary Key)
- name (String)
- email (String)
- age (Integer)
- contact (String)
- role_type (String)
- added_date (DateTime)
```

### SpecialPerson Table (Admin-added)
```python
- id (Primary Key)
- name (String)
- email (String)
- age (Integer)
- contact (String)
- role_type (String)
- added_date (DateTime)
```

### Donor Table (Admin-added)
```python
- id (Primary Key)
- name (String)
- age (Integer)
- gender (String)
- contact (String)
- address (Text)
- donation_type (String)
- amount (Float)
- preferred_time (String)
- added_date (DateTime)
```

### Donation Table (From Donors)
```python
- id (Primary Key)
- user_id (Foreign Key -> User)
- donor_name (String)
- email (String)
- phone (String)
- cnic (String)
- amount (Float)
- payment_method (String)
- date (DateTime)
- status (String)
```

### ReceivedDonation Table (Given to Beneficiaries)
```python
- id (Primary Key)
- recipient_id (Integer)
- recipient_name (String)
- recipient_email (String)
- recipient_type (senior/special)
- amount (Float)
- purpose (String)
- notes (Text)
- date (DateTime)
- given_by (String)
- status (String)
```

---

## 📸 Screenshots

### Home Page
Modern landing page with hero section, about, services, and call-to-action.

### Donor Dashboard
- Stats cards showing total donations
- Make donation button with modal form
- Complete donation history table

### Senior Dashboard
- Profile card with avatar
- Total received amount
- Received donations history
- Available services section

### Admin Dashboard
- 7 stat cards (users, seniors, donors, donations, financial tracking)
- User management tabs
- Give donations interface
- Complete transaction history

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "Module not found" Error
**Problem:** Python can't find Flask or other modules

**Solution:**
```bash
# Make sure virtual environment is activated
# Reinstall requirements
pip install -r requirements.txt
```

#### 2. "Address already in use"
**Problem:** Port 5000 is already being used

**Solution:**
```bash
# Stop other Flask apps or use different port
# In app.py, change the last line to:
app.run(debug=True, port=5001)
```

#### 3. Database Locked Error
**Problem:** SQLite database is locked

**Solution:**
```bash
# Close all other instances of the app
# Delete careconnect.db and restart
# Database will be recreated
```

#### 4. Login Not Working
**Problem:** Can't log in with credentials

**Solution:**
- Check if email is correct
- Password is case-sensitive
- Try default admin: admin@careconnect.org / admin123
- Register a new account and try

#### 5. Donations Not Showing
**Problem:** Made donation but not appearing

**Solution:**
- Refresh the page
- Check if you're logged in as correct user
- Check browser console for errors (F12)

---

## 🔧 Configuration

### Changing Secret Key

In `app.py`, change the secret key for production:

```python
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
```

Generate a secure key:
```python
import secrets
print(secrets.token_hex(32))
```

### Switching to PostgreSQL

For production, use PostgreSQL instead of SQLite:

```python
# In app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/careconnect'
```

Install psycopg2:
```bash
pip install psycopg2-binary
```

---

## 🚀 Deployment

### Deploying to Heroku

1. **Install Heroku CLI**
2. **Create Procfile:**
```
web: gunicorn app:app
```

3. **Install gunicorn:**
```bash
pip install gunicorn
pip freeze > requirements.txt
```

4. **Deploy:**
```bash
heroku create your-app-name
git push heroku main
heroku run python app.py
```

### Deploying to PythonAnywhere

1. Create account at pythonanywhere.com
2. Upload project files
3. Create virtual environment
4. Configure WSGI file
5. Set static files path

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Developer

**Your Name**
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Flask documentation and community
- Tailwind CSS for styling
- Unsplash for images
- All contributors and testers

---

## 📞 Support

If you have any questions or need help:

1. Check the [Troubleshooting](#troubleshooting) section
2. Open an issue on GitHub
3. Email: support@careconnect.org

---

## 🔄 Version History

### Version 1.0.0 (Current)
- ✅ User authentication system
- ✅ Role-based dashboards
- ✅ Donation management
- ✅ Financial tracking with balance
- ✅ Admin user management
- ✅ Complete transaction history

### Planned Features (v1.1.0)
- 📧 Email notifications
- 📊 Advanced reporting
- 📱 Mobile app
- 💳 Payment gateway integration
- 📈 Data analytics dashboard

---

**Made with ❤️ for NGOs and Social Welfare Organizations**