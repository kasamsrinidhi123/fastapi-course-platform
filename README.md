# fastapi-course-platform
# 📚 Online Course Platform (FastAPI Project)

This is a complete backend project built using FastAPI as part of my internship training.  
The project simulates a real-world **Online Course Platform** with course management, enrollments, wishlist system, and advanced APIs.

---

## 📌 Project Features

### 🔹 Core Features
- REST APIs using FastAPI
- Pydantic validation
- CRUD operations (Create, Read, Update, Delete)
- Course management system
- Enrollment workflow
- Wishlist feature

---

### 🔹 Advanced Features
- 🔍 Search functionality (case-insensitive)
- 🔄 Sorting (price, rating)
- 📄 Pagination
- 🧠 Combined browsing API (search + sort + paginate)
- 🎯 Filtering by title, instructor, category

---

## 🧠 Concepts Covered

- GET APIs
- POST APIs with validation
- Helper functions
- CRUD operations
- Workflow (Wishlist → Enrollments)
- Search, Sorting, Pagination
- Error handling using HTTPException

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
```bash
pip install -r requirements.txt
2️⃣ Run server
uvicorn main:app --reload
3️⃣ Open Swagger UI
http://127.0.0.1:8000/docs
📊 API Endpoints
📚 Course APIs

GET /courses

GET /courses/{course_id}

GET /courses/count

GET /courses/filter

GET /courses/search

GET /courses/sort

GET /courses/pagination

GET /courses/browse

POST /courses

PUT /courses/{course_id}

DELETE /courses/{course_id}

❤️ Workflow APIs

POST /wishlist/{course_id}

POST /enroll/{course_id}

GET /enrollments

GET /enrollments/browse

📸 Screenshots

All API outputs are tested using Swagger UI and stored in the screenshots/ folder.

🎯 Project Objective

To build a real-world backend system using FastAPI demonstrating:

API development

Backend logic implementation

Data handling

Workflow creation

Clean API design

🙌 Acknowledgment

Grateful for the learning opportunity at Innomatics Research Labs.

🔗 Author

Name: Srinidhi Kasam
Project: FastAPI Course Platform
Internship: FastAPI Internship
Guidance: Innomatics Research Labs

---

