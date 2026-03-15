# 🚀 Flask REST API

A clean, modular, and scalable **REST API starter template built with Flask**.
This repository provides a well-structured backend architecture that separates **routes, services, and models**, making it easy to extend and maintain.

Perfect for learning Flask APIs or bootstrapping new backend projects.

---

# ✨ Features

* ⚡ Lightweight **Flask REST API**
* 📦 Clean modular architecture
* 🔧 Environment configuration support
* 🧪 Basic testing setup
* 🗂 Organized project structure
* 🧩 Easy to scale for larger applications

---

# 📁 Project Structure

```
flask-rest-api/
│
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configuration settings
│   │
│   ├── routes/            # API routes
│   │   ├── __init__.py
│   │   └── user_routes.py
│   │
│   ├── models/            # Data models
│   │   ├── __init__.py
│   │   └── user_model.py
│   │
│   └── services/          # Business logic layer
│       ├── __init__.py
│       └── user_service.py
│
├── tests/                 # Unit tests
│   └── test_users.py
│
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-rest-api.git
cd flask-rest-api
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Mac / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flas
