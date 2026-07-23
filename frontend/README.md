# 🚗 Car Dealership Inventory Management System

<p align="center">
  <img src="https://img.shields.io/badge/React-19-blue?logo=react" />
  <img src="https://img.shields.io/badge/Django-5.x-green?logo=django" />
  <img src="https://img.shields.io/badge/Django%20REST-API-red" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql" />
  <img src="https://img.shields.io/badge/TailwindCSS-Styled-38B2AC?logo=tailwind-css" />
  <img src="https://img.shields.io/badge/JWT-Authentication-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

A modern **Full Stack Car Dealership Inventory Management System** built with **React, Django REST Framework, PostgreSQL, JWT Authentication, and Tailwind CSS**.

This application allows administrators to manage vehicle inventory efficiently while providing users with a clean and responsive interface to browse available vehicles.

---

# 📸 Screenshots

## 🔐 Login Page

> Replace with your screenshot

![Login](screenshots/login.png)

---

## 📝 Registration Page

> Replace with your screenshot

![Register](screenshots/register.png)

---

## 🚘 Dashboard

> Replace with your screenshot

![Dashboard](screenshots/dashboard.png)

---

## ➕ Add Vehicle

> Replace with your screenshot

![Add Vehicle](screenshots/add-vehicle.png)

---

## ✏️ Edit Vehicle

> Replace with your screenshot

![Edit Vehicle](screenshots/edit-vehicle.png)

---

## 🔍 Vehicle Search

> Replace with your screenshot

![Search](screenshots/search.png)

---

# ✨ Features

## Authentication

- JWT Authentication
- User Registration
- Secure Login
- Protected Routes
- Logout

---

## Vehicle Management

- Add Vehicle
- Update Vehicle
- Delete Vehicle
- Search Vehicles
- Filter Inventory
- View Vehicle Details
- Purchase Vehicle
- Restock Vehicle

---

## Dashboard

- Responsive UI
- Vehicle Cards
- Search Bar
- Loading Indicators
- Success/Error Messages

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- React Router
- Axios

## Backend

- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL

---

# 📂 Project Structure

```text
incubyte/
│
├── backend/
│   ├── config/
│   ├── users/
│   ├── vehicles/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Vighnesh0504/incubyte.git
cd incubyte
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🔑 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/auth/register/` | Register User |
| POST | `/api/auth/login/` | Login |

---

## Vehicles

| Method | Endpoint |
|---------|----------|
| GET | `/api/vehicles/` |
| POST | `/api/vehicles/` |
| GET | `/api/vehicles/:id/` |
| PATCH | `/api/vehicles/:id/` |
| DELETE | `/api/vehicles/:id/` |
| POST | `/api/vehicles/:id/purchase/` |
| POST | `/api/vehicles/:id/restock/` |
| GET | `/api/vehicles/search/` |

---

# 🔒 Authentication

JWT authentication is used.

After login, the frontend stores:

- Access Token
- Refresh Token
- Username

Protected endpoints require:

```
Authorization: Bearer <access_token>
```

---

# 📈 Future Improvements

- Pagination
- Image Upload
- Vehicle Categories
- Dark Mode
- User Roles
- Refresh Token Rotation
- Docker Deployment
- CI/CD Pipeline

---

# 💻 Developed By

**Vighnesh Pawar**

Artificial Intelligence & Machine Learning Engineer

GitHub:
https://github.com/Vighnesh0504

