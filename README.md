#  Blog API with Pagination, Search & Sorting

##  Description
This is a Django REST Framework (DRF) Blog API that supports CRUD operations with **pagination, search, filtering, and sorting**.  
It’s built to handle large datasets efficiently and provide a clean developer experience.

---

##  Setup & Run Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd blog_api
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply Migrations & Start Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

---

##  Example API Requests & Responses

### 1. Get Paginated Posts (default page=1, limit=10)
**Request**
```http
GET /posts/
```
**Response**
```json
{
  "total_posts": 25,
  "total_pages": 3,
  "current_page": 1,
  "results": [
    {
      "id": 1,
      "title": "First Post",
      "content": "This is the first blog post",
      "author": "Admin",
      "created_at": "2025-08-15T12:00:00Z"
    }
  ]
}
```

### 2. Get Paginated Posts – Custom Limit
**Request**
```http
GET /posts/?page=2&limit=5
```

### 3. Search Posts by Title or Content
**Request**
```http
GET /posts/?search=django
```

**Response**
```json
{
  "total_posts": 2,
  "total_pages": 1,
  "current_page": 1,
  "results": [
    {
      "id": 3,
      "title": "Django API Guide",
      "content": "Learn how to build APIs with Django REST Framework",
      "author": "Raja",
      "created_at": "2025-08-15T14:00:00Z"
    }
  ]
}
```

### 4. Search + Pagination Combined
**Request**
```http
GET /posts/?search=api&page=1&limit=2
```

---

## 📥 Postman Collection

You can import the provided Postman collection to test pagination and search directly.

File: `blog_api.postman_collection.json`

It contains the following requests:
1. **Get Paginated Posts (default)**  
2. **Get Paginated Posts – Custom Limit**  
3. **Search Posts by Title or Content**  
4. **Search + Pagination Combined**  

In Postman, go to **File → Import → Upload Files** and select the JSON collection file.

---

##  Summary
- **Pagination**: `?page` and `?limit`  
- **Search**: `?search=keyword`  
- **Combine**: `?search=keyword&page=2&limit=5`  

This ensures an optimized API experience for large-scale blog applications.
