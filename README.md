# 🚀 FastAPI Course Platform

This project is developed using **FastAPI** as part of my internship training at Innomatics Research Labs.

It simulates a real-world **Online Course Platform** where users can manage courses, search, filter, sort, and enroll.

---

## 📌 Features

### 🔹 Core Features

* REST APIs using FastAPI
* Pydantic validation
* CRUD operations
* Course management system

### 🔹 Advanced Features

* 🔍 Search functionality
* 🔄 Sorting (price, rating)
* 📄 Pagination
* 🎯 Filter API (title, instructor, category)
* 🧠 Combined browsing API (search + sort + pagination)

---

## 🧠 Concepts Covered

* FastAPI framework
* Pydantic models
* API design
* CRUD operations
* Query parameters
* Search, Sorting, Pagination
* Workflow implementation (Wishlist & Enrollment)

---

## 🗂️ Project Structure

fastapi-course-platform/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/

---

## ⚙️ Installation & Run

### 1️⃣ Install dependencies

pip install -r requirements.txt

### 2️⃣ Run server

uvicorn main:app --reload

### 3️⃣ Open Swagger UI

http://127.0.0.1:8000/docs

---

## 📊 API Endpoints

### 📚 Course APIs

* GET /courses
* GET /courses/{course_id}
* GET /courses/count
* GET /courses/filter
* GET /courses/search
* GET /courses/sort
* GET /courses/pagination
* GET /courses/browse
* POST /courses
* PUT /courses/{course_id}
* DELETE /courses/{course_id}

### ❤️ Workflow APIs

* POST /wishlist/{course_id}
* POST /enroll/{course_id}
* GET /enrollments
* GET /enrollments/browse

---

## 📸 Screenshots

Swagger UI outputs are stored in the **screenshots/** folder.

---

## 🎯 Objective

To build a real-world backend system demonstrating API development, backend logic, and workflow implementation using FastAPI.

---

## 🙌 Acknowledgment

Thanks to **Innomatics Research Labs** for guidance and support.

---

## 👩‍💻 Author

**Srinidhi Kasam**
FastAPI Internship Project

---

## ⭐ Final Note

This project showcases my understanding of backend development and API design using FastAPI.
