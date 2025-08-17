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

## PROJECT-DEMO ##

<img width="1374" height="673" alt="1" src="https://github.com/user-attachments/assets/ee68232a-0d9a-4389-a86b-cd67743a6250" />
<img width="1444" height="901" alt="2" src="https://github.com/user-attachments/assets/7275d9af-fee6-403b-a1e9-8002d9ffe8bc" />
<img width="1392" height="778" alt="3" src="https://github.com/user-attachments/assets/8dacf377-d1a1-41d9-a18f-101106fc2980" />
<img width="1452" height="816" alt="4" src="https://github.com/user-attachments/assets/65441182-1980-494d-a528-c5c2c45080d7" />
<img width="1455" height="920" alt="5" src="https://github.com/user-attachments/assets/8de29846-3515-4bbc-b91c-294b0da53fd4" />
<img width="1436" height="896" alt="6" src="https://github.com/user-attachments/assets/1fda310c-24b6-4f1e-a415-c5065c0bd44f" />
<img width="1450" height="898" alt="7" src="https://github.com/user-attachments/assets/f57fe77f-4b4e-42ad-a702-885595639968" />
<img width="1433" height="887" alt="8" src="https://github.com/user-attachments/assets/9a394f28-0601-4140-a9e2-249cf6762126" />
<img width="1461" height="879" alt="9" src="https://github.com/user-attachments/assets/8972816c-60d4-4cbe-a216-fb77699a3f21" />
<img width="1461" height="477" alt="10" src="https://github.com/user-attachments/assets/4ac424d0-3a01-444e-bde0-6b6868a4caf6" />
<img width="1426" height="590" alt="11" src="https://github.com/user-attachments/assets/d84f2fa6-a36e-4af1-b2ef-cf8f9eb54273" />
<img width="1439" height="404" alt="12" src="https://github.com/user-attachments/assets/b1864782-cc22-465d-a3f7-68a1efe1c4a5" />
<img width="1447" height="373" alt="13" src="https://github.com/user-attachments/assets/dda4c915-abe9-4544-b08e-ceeb5e6e9998" />
<img width="1449" height="401" alt="14" src="https://github.com/user-attachments/assets/4d59936f-0f26-4fa5-9819-72e29c6ce9ae" />
<img width="1447" height="420" alt="15" src="https://github.com/user-attachments/assets/74ce851f-9fde-4a54-bec9-bdb291867187" />

 
