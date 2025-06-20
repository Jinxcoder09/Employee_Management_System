# Employee_Management_System

A Django-based employee management system with PostgreSQL, REST APIs, token authentication, and interactive Chart.js visualizations. Built for seamless deployment on **Railway**.

---

## 🔍 Project Overview

This system provides:

- Employee & Department management
- Attendance & Performance tracking
- RESTful APIs with Swagger & Redoc docs
- Token-based user authentication
- A Dashboard with interactive charts

---

## 🧱 Tech Stack

- **Backend:** Django 5, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** Token Authentication
- **Docs:** Swagger & Redoc via drf-yasg
- **Frontend:** Django Templates + Chart.js
- **Deployment:** Railway + Gunicorn + Nixpacks
- **Extras:** WhiteNoise, CORS, .env support via `django-environ`

---

## 📦 Features

✅ REST APIs for:
- Employees
- Departments
- Attendance
- Performance

✅ Token-based authentication

✅ Interactive dashboard with:
- Employees per department (Pie Chart)
- Monthly attendance trends (Bar Chart)
- Department average performance (Bar Chart)
- Top 5 attendance ranking (Bar Chart)

✅ Admin panel

✅ Swagger & Redoc documentation

✅ Seed endpoints for demo data

✅ Clean UI with a fixed responsive navbar

---

## ✨ Getting Started (Local Setup)

### 1. Clone the repository


git clone https://github.com/Jinxcoder09/Employee_Management_System.git
cd Employee_Management_System

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt

4. Add a .env file at the root
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://username:password@localhost:5432/dbname
CORS_ALLOWED_ORIGINS=http://127.0.0.1:8000

5. Run migrations and collect static files

python manage.py migrate
python manage.py collectstatic --noinput

6. Create superuser
python manage.py createsuperuser
🔗 Key Endpoints
Path	Description
/	Dashboard with charts
/admin/	Django admin panel
/api/	API root
/api/employees/	CRUD for employees
/api/departments/	CRUD for departments
/api/attendance/	Attendance records
/api/performance/	Performance scores
/api-token-auth/	Get token (POST username/password)
/swagger/	Swagger API documentation
/redoc/	Redoc API documentation
/create-superuser/	Auto-creates a default admin user

## 📊 Dashboard Visualizations
Accessible at /, includes:

Pie Chart: Employees per department

Bar Chart: Monthly attendance overview

Bar Chart: Average performance by department

Bar Chart: Top 5 employees by attendance

## ☁️ Deployment on Railway
🧰 Railway Setup
Create a Railway project

Add PostgreSQL plugin → this sets DATABASE_URL

Set the following Railway environment variables:


SECRET_KEY=your-secret
DEBUG=False
ALLOWED_HOSTS=your-app.up.railway.app
CORS_ALLOWED_ORIGINS=https://your-app.up.railway.app
CSRF_TRUSTED_ORIGINS=https://your-app.up.railway.app
DATABASE_URL=postgres://user:pass@host:port/dbname
Push to Railway via GitHub or CLI

Railway auto-detects build and run steps via Nixpacks

## 🔥 Production Commands

python manage.py migrate
python manage.py collectstatic --noinput
Seed demo data if needed:


curl https://greentree.up.railway.app/create-superuser/
✅ Best Practices
✅ Keep SECRET_KEY safe

❌ Don’t set DEBUG=True in production

✅ Use TokenAuthentication for APIs

✅ Use .env for environment-specific secrets

✅ Lock down /create-superuser/ or remove after use

## 📸 Screenshots

Add screenshots here once you host the dashboard.

## 👨‍💻 Author
Manish Kumar

GitHub: @Jinxcoder09


🙌 Support

Found this helpful? Give it a ⭐ on GitHub!
