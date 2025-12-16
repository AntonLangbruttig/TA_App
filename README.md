# TA Management System

A full-stack Django web application for managing teaching assistants, courses, and lab assignments. Built as a team project for the Software Engineering course at UW-Milwaukee.

## Features

- **User Authentication** — Login system with Django session management
- **Role-Based Access Control** — Three user roles (Supervisor, Instructor, TA) with different permissions
- **Relational Database** — 4 models with foreign key relationships
- **Full CRUD Operations** — 11 view classes for accounts, courses, and sections
- **TA Assignment System** — Assign TAs to courses with grader status and lab capacity tracking
- **Course Section Scheduling** — Manage Lecture, Lab, and Discussion sections with time/day selection
- **Comprehensive Testing** — 11 test files (4 unit + 7 acceptance tests)

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Django Templates
- **Version Control:** Git

## Database Models

| Model | Key Fields |
|-------|------------|
| User | username, role, email, phone, office hours, skills |
| Course | course ID, name, credits, instructor (FK) |
| TA | user (FK), grader status, num labs, assigned labs |
| Section | course (FK), type, schedule, TA assigned (FK) |

## User Roles

| Role | Permissions |
|------|-------------|
| Supervisor | Full access — manage all users, courses, sections, and assignments |
| Instructor | View and manage assigned courses and TAs |
| TA | View course assignments and section schedules |

## Project Structure
```
TA_App/
├── project/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── project_app/             # Main application
│   ├── models.py            # User, Course, TA, Section models
│   ├── views.py             # 11 view classes
│   └── migrations/
├── Classes/
│   └── functions.py         # Business logic helpers
├── templates/               # 14 HTML templates
├── static/css/              # 14 CSS files
├── UnitTests/               # 4 unit test files
├── AcceptanceTests/         # 7 acceptance test files
└── manage.py
```

## Testing
```bash
python manage.py test UnitTests
python manage.py test AcceptanceTests
```

**Test Coverage:**
- `test_user.py` — User creation and validation
- `test_course.py` — Course CRUD operations
- `test_lab.py` — Lab/section management
- `test_edit_account.py` — Account editing
- 7 acceptance tests for end-to-end workflows

## Running Locally
```bash
# Clone the repository
git clone https://github.com/AntonLangbruttig/TA_App.git
cd TA_App

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Open http://localhost:8000

## Team

Built collaboratively by a team of 5 developers as part of UW-Milwaukee's Software Engineering curriculum.

## License

This project was created for educational purposes at UW-Milwaukee.
