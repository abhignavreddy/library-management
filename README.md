# **Library Management System (Django REST Framework)**

This is a **Library Management System** built using **Django** and **Django REST Framework (DRF)**.  
It allows admins to **manage books** while providing public access for users to view available books.

---

## 🚀 **Features**
✅ **Admin authentication** (JWT-based login & signup)  
✅ **Add, update, and delete books** (Admin-only)  
✅ **View all books** (Public API)  
✅ **Pagination & Sorting** options  
✅ **Custom error handling** (404 Not Found & 401 Unauthorized)  
✅ **API documentation** using **Swagger & ReDoc**  

---

## 🛠️ **Setup & Installation**  

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/library-management.git
cd library-management
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 💾 **Database Setup (MySQL)**
### **4️⃣ Install MySQL & Configure Database**
- Install MySQL Server & Workbench if not installed.
- Create a database named **`library_db`** in MySQL.

**Update `DATABASES` in `settings.py`:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',  # Your database name
        'USER': 'root',        # Your MySQL username
        'PASSWORD': 'yourpassword',  # Your MySQL password
        'HOST': 'localhost',   # Server address
        'PORT': '3306',        # MySQL port (default is 3306)
    }
}
```

### **5️⃣ Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

---

##  **Admin Authentication**
### **6️⃣ Create a Superuser (Admin)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### **7️⃣ Run the Server**
```sh
python manage.py runserver
```
Your API will be available at:  
`http://127.0.0.1:8000/api/`

---

# ** API Endpoints**

##  **Admin Authentication (JWT-Based)**

### **📌 Admin Signup**
**Endpoint:**  
```
POST /api/admin/signup/
```
**Request Body (JSON):**
```json
{
  "username": "admin1",
  "email": "admin1@example.com",
  "password": "securepass123"
}
```
**Response:**
```json
{
  "message": "Admin registered successfully!"
}
```

---

### ** Admin Login**
**Endpoint:**  
```
POST /api/admin/login/
```
**Request Body (JSON):**
```json
{
  "username": "admin1",
  "password": "securepass123"
}
```
**Response:**
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```
**Use this token in API requests:**
```
Authorization: Bearer your_access_token
```

---

##  **Books API**

### **📌 Get All Books (Public)**
**Endpoint:**  
```
GET /api/books/
```
**Query Parameters (Optional):**
- `page_size=5` → Number of books per page  
- `sort_by=title` → Sort by `id` (default) or `title`  

---

### **📌 Add a Book (Admin)**
**Endpoint:**  
```
POST /api/books/
```
**Headers:**
```
Authorization: Bearer your_access_token
```
**Request Body (JSON):**
```json
{
  "title": "Django 3 By Example",
  "author": "Antonio Melé",
  "published_date": "2020-03-31",
  "isbn": "9781838981952"
}
```
**Response:**
```json
{
  "id": 2,
  "title": "Django 3 By Example",
  "author": "Antonio Melé",
  "published_date": "2020-03-31",
  "isbn": "9781838981952"
}
```

---

### **📌 Get Book by ID (Protected)**
```sh
GET /api/books/{book_id}/
```

---

### **📌 Update a Book (Protected)**
```sh
PUT /api/books/{book_id}/
```

---

### **📌 Delete a Book (Protected)**
```sh
DELETE /api/books/{book_id}/
```
**Response:**
```json
{
  "message": "Successfully deleted"
}
```

---

#  **API Documentation**

📌 **Swagger UI:**  
[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

📌 **ReDoc UI:**  
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## ❌ **Error Handling**
If an invalid request is made, the API returns a structured JSON error message:

### **🔴 404 - Resource Not Found**
```json
{
  "error": "The requested resource was not found."
}
```

### **🔴 401 - Unauthorized**
```json
{
  "error": "Unauthorized access. Please log in."
}
```

---

## 🔄 **Token Management**
### **📌 Refresh Access Token**
**Endpoint:**  
```
POST /api/admin/token/refresh/
```
**Request Body (JSON):**
```json
{
  "refresh": "your_refresh_token"
}
```
**Response:**
```json
{
  "access": "new_access_token"
}
```

---

#  **Project Structure**
```
libraryManagement/
│
├── books/  # Books app
│   ├── models.py  # Book model
│   ├── views.py  # API views for books
│   ├── serializers.py  # DRF serializers
│   ├── urls.py  # URL mappings for books
│   ├── admin.py  # Admin panel configuration
│
├── libraryManagement/  # Main Django project
│   ├── settings.py  # Project settings
│   ├── urls.py  # API routes
│   ├── wsgi.py  # WSGI entry point
│   ├── middleware.py  # Custom authentication middleware
│   ├── error_handlers.py  # Custom error handlers
│
├── static/  # Static files
├── .env  # Environment variables (SECRET_KEY, DB credentials)
├── manage.py  # Django CLI tool
└── requirements.txt  # Dependencies
```

---
