# 🚀 FastAPI Tutorial

Welcome to the FastAPI Tutorial repository! This project is designed as a structured guide and hands-on resource for my colleagues to learn and master building high-performance web APIs using FastAPI.

---

## 🛠️ Tech Stack & Prerequisites
* **Python** (v3.9 or higher recommended)
* **FastAPI** (The modern, fast web framework)
* **Uvicorn** (The lightning-fast ASGI server)
* **Pydantic** (For data validation and settings management)

---

## ⚙️ Getting Started

Follow these steps to set up the tutorial project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd fastapiTutorial
```

### 2. Set Up a Virtual Environment
It is highly recommended to isolate your dependencies using a virtual environment.
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn
```
*(If a `requirements.txt` file is present, run: `pip install -r requirements.txt`)*

### 4. Run the Development Server
Start the application using Uvicorn:
```bash
uvicorn main:app --reload
```
* The `--reload` flag enables auto-reload so the server refreshes automatically when you make changes to the code.
* Open your browser and navigate to: **`http://127.0.0.1:8000`**

---

## 📑 Interactive API Documentation

One of FastAPI's best features is its automatic, interactive documentation. Once your server is running, you can access:

* **Interactive Swagger UI:** `http://127.0.0` (Great for testing endpoints directly in the browser)
* **Alternative ReDoc UI:** `http://127.0.0` (Clean, detailed API reference documentation)

---

## 🎓 Tutorial Syllabus / Modules

This repository covers the following fundamental FastAPI concepts:
* 🟢 **Module 1:** Setting up your first path operation (`Hello World`)
* 🟢 **Module 2:** Path Parameters vs. Query Parameters
* 🟢 **Module 3:** Request Bodies and Data Validation using **Pydantic**
* 🟢 **Module 4:** Handling HTTP Status Codes & Error Responses
* 🟢 **Module 5:** Connecting to a Database (SQLAlchemy / Tortoise ORM) *(Optional/Upcoming)*

---

## 🤝 Contributing
If you are one of my colleagues taking this tutorial and want to add exercises, fix typos, or suggest additions:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
