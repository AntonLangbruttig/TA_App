# TA Management System

A full-stack Django web application for managing teaching assistants, courses, and lab assignments. Built as a team project for the Software Engineering course at UW-Milwaukee.

## Features

- **User Authentication** — Login system with session management and protected routes
- **Role-Based Access Control** — Three user roles (Supervisor, Instructor, TA) with different permission levels
- **Database Design** — 4 related tables with foreign key relationships (Users, Courses, TAs, Sections)
- **Full CRUD Operations** — Create, read, update, and delete functionality for accounts, courses, and sections
- **TA Assignment System** — Assign TAs to courses with lab capacity tracking
- **Course Section Scheduling** — Manage Lecture, Lab, and Discussion sections with scheduling
- **Comprehensive Unit Tests** — Test coverage for core functionality

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Django Templates
- **Version Control:** Git

## User Roles

| Role | Permissions |
|------|-------------|
| Supervisor | Full access — manage all users, courses, sections, and assignments |
| Instructor | View and manage their assigned courses and TAs |
| TA | View their course assignments and section schedules |

## Project Structure

```
TA_App/
├── TA_APP/
│   ├── models.py        # Database models (User, Course, TA, Section)
│   ├── views.py         # View functions for all routes
│   ├── functions.py     # Business logic and helper functions
│   └── tests.py         # Unit tests
├── templates/           # HTML templates
├── manage.py
└── README.md
```

## Running Locally

1. Clone the repository
```bash
git clone https://github.com/AntonLangbruttig/TA_App.git
cd TA_App
```

2. Install dependencies
```bash
pip install django
```

3. Run migrations
```bash
python manage.py migrate
```

4. Start the development server
```bash
python manage.py runserver
```

5. Open http://localhost:8000 in your browser

## Team

Built collaboratively by a team of 5 developers as part of UW-Milwaukee's Software Engineering curriculum.

## License

This project was created for educational purposes at UW-Milwaukee.
