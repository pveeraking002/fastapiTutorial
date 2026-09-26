FastAPI Tutorial

A beginner-friendly tutorial for learning FastAPI, a modern, fast Python web framework for building APIs.

📚 What You'll Learn

By completing this tutorial, you will learn how to:

Set up a FastAPI project

Create your first API

Define GET, POST, PUT, and DELETE endpoints

Use path and query parameters

Validate request data with Pydantic

Work with request and response models

Handle errors and HTTP status codes

Connect FastAPI to a database

Use dependency injection

Add authentication

Test FastAPI applications

Run and deploy a FastAPI application

🛠️ Prerequisites

Before starting, make sure you have:

Python 3.10+

Basic knowledge of Python

Basic understanding of REST APIs

Git installed

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/fastapi-tutorial.git
cd fastapi-tutorial

2. Create a virtual environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

📁 Project Structure
fastapi-tutorial/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routes/
│       ├── __init__.py
│       └── users.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
├── .gitignore
└── README.md

▶️ Run the Application

Start the development server with:

uvicorn app.main:app --reload


The API will be available at:

http://127.0.0.1:8000

📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

Open:

http://127.0.0.1:8000/docs

ReDoc

Open:

http://127.0.0.1:8000/redoc

🧑‍💻 Your First FastAPI Application

Create app/main.py:

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


Run the application:

uvicorn app.main:app --reload


Then visit:

http://127.0.0.1:8000


You should receive:

{
  "message": "Hello, FastAPI!"
}

🔌 API Examples
GET Request
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


Example:

GET /users/10

Query Parameters
@app.get("/users")
def search_users(name: str | None = None):
    return {"name": name}


Example:

GET /users?name=Alice

POST Request

Using Pydantic:

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    return user


Example request:

{
  "name": "Alice",
  "email": "alice@example.com"
}

🗄️ Database

The tutorial can be extended to use a database such as:

SQLite

PostgreSQL

MySQL

A typical application can use SQLAlchemy or another database library to manage database operations.

🧪 Testing

Install testing dependencies:

pip install pytest httpx


Example test:

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


Run tests:

pytest

🔐 Authentication

Later sections of the tutorial cover authentication and authorization, including:

OAuth2

JWT tokens

Password hashing

Protected routes

User authentication

📋 Tutorial Roadmap

 Introduction to FastAPI

 Project setup

 First API endpoint

 Path parameters

 Query parameters

 Request bodies

 Pydantic models

 Response models

 Error handling

 CRUD APIs

 Database integration

 Dependency injection

 Authentication

 Testing

 Deployment

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

git checkout -b feature/my-feature


Make your changes

Commit your changes

git commit -m "Add new FastAPI tutorial"


Push your branch

git push origin feature/my-feature


Open a Pull Request

📄 License

This project is available under the MIT License.

⭐ Support

If this tutorial helped you learn FastAPI, consider giving the repository a ⭐ on GitHub.
