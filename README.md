# 📝 Todo App (Full-Stack Version)

A full-featured todo app with user authentication and a SQLite database.

## Features
- ✅ User registration and login
- ✅ Session management (Flask-Login)
- ✅ Personal todo lists per user
- ✅ Full CRUD via REST API
- ✅ Secure password hashing (bcrypt)
- ✅ Polished UI with Bootstrap

## Tech Stack
- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite

## Run Locally

```bash
# Clone the repo
git clone https://github.com/Ajtech27/todo-app-auth.git
cd todo-app-auth

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py