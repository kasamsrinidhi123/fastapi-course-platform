# 🚀 FastAPI Online Course Platform

This project is developed using **FastAPI** as part of my internship training at **Innomatics Research Labs**.

It simulates a real-world **Online Course Platform** where users can manage courses, search, filter, sort, and enroll in courses.

---

## 📌 Features

### 🔹 Core Features

* REST APIs using FastAPI
* Pydantic validation
* CRUD operations (Create, Read, Update, Delete)
* Course management system

### 🔹 Advanced Features

* 🔍 Search functionality (case-insensitive)
* 🔄 Sorting (price, rating)
* 📄 Pagination
* 🎯 Filter API (title, instructor, category)
* 🧠 Combined browsing API (search + sort + pagination)

---

## 🧠 Concepts Covered

* FastAPI framework
* Pydantic models & validation
* API design and structure
* CRUD operations
* Query parameters
* Search, Sorting, Pagination
* Multi-step workflows (Wishlist → Enrollment)
* Error handling using HTTPException

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

### Workflow APIs

* POST /wishlist/{course_id}
* POST /enroll/{course_id}
* GET /enrollments
* GET /enrollments/browse

---

## 📸 Screenshots

All API outputs are tested using Swagger UI and stored in the **screenshots/** folder.

---

## 🎯 Project Objective

To build a real-world backend system using FastAPI demonstrating API design, backend logic, data handling, and workflow implementation.

---

## 🙌 Acknowledgment

Grateful for the learning opportunity at **Innomatics Research Labs**.

---

## 👩‍💻 Author

**Name:** Srinidhi Kasam  
**Project:** FastAPI Online Course Platform  
**Internship:** FastAPI Internship  
**Guidance under:** @Innomatics Research Labs

---

## ⭐ Final Note

This project showcases my understanding of backend development and API design using FastAPI.
