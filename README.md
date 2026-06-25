# Rivyou Product Search API

##  Intelligent Product Search API

A Django REST Framework-based Product Search API that provides secure JWT authentication and intelligent product search functionality. This project allows users to register, log in, retrieve products, and search products using keyword matching, category filtering, and relevance scoring.

---

# Features

* User Registration
* JWT Authentication (Login)
* Protected API Endpoints
* Product Listing API
* Intelligent Product Search
* Keyword-based Search
* Category Filtering
* Search Result Limiting
* Relevance Score Calculation
* Swagger API Documentation
* ReDoc API Documentation

---

# Tech Stack

* Python 3.14
* Django 5/6
* Django REST Framework
* Simple JWT
* SQLite3
* drf-yasg (Swagger & ReDoc)

---

# Project Structure

```
rivyou-assignment/
│
├── authentication/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── products_data.csv
├── requirements.txt
├── README.md
└── db.sqlite3
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to the project

```bash
cd rivyou-assignment
```

Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

Server will start at

```
http://127.0.0.1:8000/
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

---

# Authentication

This project uses JWT Authentication.

### Register User

**POST**

```
/api/auth/register/
```

Example Request

```json
{
    "username":"john",
    "email":"john@example.com",
    "password":"123456"
}
```

---

### Login

**POST**

```
/api/auth/login/
```

Example Request

```json
{
    "username":"john",
    "password":"123456"
}
```

Response

```json
{
    "refresh":"<refresh_token>",
    "access":"<access_token>"
}
```

Use the Access Token in Swagger by clicking **Authorize** and entering:

```
Bearer <access_token>
```

---

# Product APIs

## Get All Products

**GET**

```
/api/products/
```

Returns the complete list of products.

---

## Search Products

**GET**

```
/api/products/search/
```

### Query Parameters

| Parameter       | Description                |
| --------------- | -------------------------- |
| q               | Search keyword             |
| limit           | Maximum number of results  |
| category_filter | Filter by product category |

Example

```
/api/products/search/?q=smartphone&limit=10&category_filter=Smartphones
```

---

# Search Features

The search engine supports

* Keyword Matching
* Category Filtering
* Tag Matching
* Relevance Scoring
* Ranking of Search Results

Each search response includes

* Product Information
* Matching Tags
* Relevance Score
* Rank Reason

---

# HTTP Status Codes

| Code | Description      |
| ---- | ---------------- |
| 200  | Success          |
| 201  | Resource Created |
| 400  | Bad Request      |
| 401  | Unauthorized     |
| 404  | Not Found        |

---

## API Endpoints

| Method | Endpoint | Authentication |
|--------|----------|----------------|
| POST | /api/auth/register/ | No |
| POST | /api/auth/login/ | No |
| GET | /api/products/ | Yes |
| GET | /api/products/search/ | Yes |

# Sample Workflow

1. Register a new user.
2. Log in using the registered credentials.
3. Copy the JWT Access Token.
4. Click **Authorize** in Swagger.
5. Enter

```
Bearer <access_token>
```

6. Access protected Product APIs.
7. Search products using keywords and filters.

---

# Future Improvements

* Pagination
* Product Sorting
* Advanced Search Ranking
* Unit Testing
* Docker Support
* PostgreSQL Integration

---

# Author

**Kushal Raj U R**

B.E. Information Science & Engineering

AMC Engineering College

Internship Assignment – Rivyou Product Search API
