from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# ------------------ DATABASE ------------------
courses = []
enrollments = []
wishlist = []

# ------------------ MODELS ------------------
class Course(BaseModel):
    id: int
    title: str = Field(min_length=3)
    instructor: str
    price: float = Field(gt=0)
    rating: float = Field(ge=0, le=5)
    category: str

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    instructor: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[float] = None
    category: Optional[str] = None

# ------------------ HELPERS ------------------
def find_course(course_id: int):
    for c in courses:
        if c["id"] == course_id:
            return c
    return None

def filter_courses(title=None, instructor=None, category=None):
    result = courses
    if title is not None:
        result = [c for c in result if title.lower() in c["title"].lower()]
    if instructor is not None:
        result = [c for c in result if instructor.lower() in c["instructor"].lower()]
    if category is not None:
        result = [c for c in result if category.lower() in c["category"].lower()]
    return result

# ------------------ DAY 1 ------------------
@app.get("/")
def home():
    return {"message": "Online Course Platform API"}

@app.get("/courses")
def get_courses():
    return courses

@app.get("/courses/count")
def count_courses():
    return {"total_courses": len(courses)}

# ------------------ IMPORTANT: FIXED ROUTES FIRST ------------------

@app.get("/courses/filter")
def filter_api(
    title: Optional[str] = Query(None),
    instructor: Optional[str] = Query(None),
    category: Optional[str] = Query(None)
):
    return filter_courses(title, instructor, category)

@app.get("/courses/search")
def search_courses(q: str):
    result = [
        c for c in courses
        if q.lower() in c["title"].lower() or q.lower() in c["category"].lower()
    ]
    if not result:
        return {"message": "No results found"}
    return result

@app.get("/courses/sort")
def sort_courses(sort_by: str = "price", order: str = "asc"):
    if sort_by not in ["price", "rating"]:
        raise HTTPException(400, "Invalid sort field")

    reverse = True if order == "desc" else False
    return sorted(courses, key=lambda x: x[sort_by], reverse=reverse)

@app.get("/courses/pagination")
def paginate(page: int = 1, limit: int = 2):
    total = len(courses)
    total_pages = (total + limit - 1) // limit

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": courses[start:end]
    }

@app.get("/courses/browse")
def browse_all(
    q: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 2
):
    result = courses

    if q:
        result = [c for c in result if q.lower() in c["title"].lower()]

    if sort_by in ["price", "rating"]:
        reverse = True if order == "desc" else False
        result = sorted(result, key=lambda x: x[sort_by], reverse=reverse)

    total = len(result)
    total_pages = (total + limit - 1) // limit

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": result[start:end]
    }

# ------------------ VARIABLE ROUTES ------------------

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")
    return course

# ------------------ DAY 2 ------------------
@app.post("/courses", status_code=201)
def add_course(course: Course):
    if find_course(course.id):
        raise HTTPException(400, "Course already exists")
    courses.append(course.dict())
    return course

# ------------------ DAY 4 ------------------
@app.put("/courses/{course_id}")
def update_course(course_id: int, updated: CourseUpdate):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    for key, value in updated.dict(exclude_none=True).items():
        course[key] = value

    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    for e in enrollments:
        if e["id"] == course_id:
            raise HTTPException(400, "Cannot delete enrolled course")

    courses.remove(course)
    return {"message": "Deleted successfully"}

# ------------------ DAY 5 WORKFLOW ------------------
@app.post("/wishlist/{course_id}")
def add_to_wishlist(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    wishlist.append(course)
    return {"message": "Added to wishlist"}

@app.post("/enroll/{course_id}")
def enroll_course(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    enrollments.append(course)
    return {"message": "Enrolled successfully"}

@app.get("/enrollments")
def get_enrollments():
    return enrollments

@app.get("/enrollments/browse")
def browse_enrollments(page: int = 1, limit: int = 2):
    total = len(enrollments)
    total_pages = (total + limit - 1) // limit

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": enrollments[start:end]
    }