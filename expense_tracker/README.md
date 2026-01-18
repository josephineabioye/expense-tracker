# Expense Tracker

A simple **Flask-based CRUD application** for tracking expenses, fully containerized with Docker.

This project demonstrates:

- Python + Flask backend
- CRUD functionality (Create, Read, Update, Delete)
- Docker containerization for consistent environment
- Git version control and clean project structure

---

## **Features**

- Add, edit, delete, and view expenses
- Organized templates and static files
- Runs locally or inside a Docker container

---

## **Getting Started**

### **Prerequisites**

- Python 3.11+ (if running locally)
- Docker (for containerized setup)
- Git

---

### **Run Locally (without Docker)**

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

5. Open your browser:
```bash
http://localhost:5000
```

### **Run with Docker**

1. Build the Docker image:
```bash
docker build -t expense_tracker .
```

2. Run the container:
```bash
docker run -p 5001:5000 expense_tracker
```

3. Open your browser:
```bash
http://localhost:5001
```

### Project Structure

expense_tracker/
├── app.py               # Main Flask app
├── Dockerfile           # Docker instructions
├── requirements.txt     # Python dependencies
├── .dockerignore        # Files/folders to ignore in Docker
├── templates/           # HTML templates
├── static/              # CSS, JS, images
└── (venv/ is ignored)   # Virtual environment


