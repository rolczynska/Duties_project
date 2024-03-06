# Overview
This app lets groups or families create tasks and categories, assign tasks to members, and mark them as completed. Built for an interview task, it simplifies managing group chores and activities.
## Technologies
- Python
- Django
- Django REST Framework
- Docker
## Features
- Task Management: Utilizes Category and Task models to organize tasks.
- User Association: Employs the User model to link tasks with specific users.
- Secure Access: Uses Django's built-in Basic Authentication to ensure that only authenticated users can modify tasks.

Currently, the project functions as an API-driven platform, providing RESTful endpoints for task and category management with secure, authenticated access.

## Future Improvments
- Enhanced Authentication: Plans to introduce login/registration and token-based authorization.
- User Interface: Plans to build a single-page web interface with frontend for easier task and activity management.

# Quick Start

This project leverages Docker for easy setup, automatically initializing users, categories, and tasks using a fixtures file. For development and testing phases. Make sure you have Docker installed on your system.
  
1. **Clone the repository from GitHub**
```
git clone git@github.com:rolczynska/duties_project.git
```

2. **Build the Image**:

Navigate to project directory and run:
```
docker build -t duties_project .
```
3. **Start the Container**:
```
docker run -d -p 8000:8000 duties_project
```
4. **Access the app**
   
Navigate at http://localhost:8000.

# API Endpoints

The API offers RESTful endpoints for categories, tasks, and users, supporting CRUD operations with authentication for secure access.

- Categories: /categories/ and /categories/{id}/
- Tasks: /tasks/ and /tasks/{id}/
- Users: /users/ and /users/{id}/

Use HTTP clients like Postman or cURL for API interactions. Authenticate CRUD operations with Basic Auth credentials.

## cURL Examples

- List Tasks:
```
curl http://127.0.0.1:8000/tasks/
```
- Get Task Details:
```
curl http://127.0.0.1:8000/tasks/1/
```
- List Users:
```
curl http://127.0.0.1:8000/users/
```
- Get User Details
(should contain only task 5):
```
curl http://127.0.0.1:8000/users/4/
```
- Create Task (without Auth - it should fail):
```
curl -X POST -H 'Content-Type: application/json' -d '{"title": "Vacuum living room", "description": "Vacuum the entire living room.", "category":1, "assigned_to": 4}' http://127.0.0.1:8000/tasks/
```
- Create Task
(with correct Auth - it should add task 7):
```
curl -X POST -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"title": "Vacuum living room", "description": "Vacuum the entire living room.", "category":1, "assigned_to": 4}' http://127.0.0.1:8000/tasks/
```
- Modify Task 7
("title": "Vacuum living room" -> "title": "PLEASE vacuum living room"):
```
curl -X PUT -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"title": "PLEASE vacuum living room", "description": "Vacuum the entire living room.", "category":1, "assigned_to": 4}' http://127.0.0.1:8000/tasks/7/
```
- Update Task 7
("completed": false -> "completed": true):

! Note that tasks are ordered by completion and date - completed task go to the end.
```
curl -X PATCH -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"completed": true}' http://127.0.0.1:8000/tasks/7/
```
- Get User Details
(users tasks should contain task 5 and 7):
```
curl http://127.0.0.1:8000/users/4/
```
- Delete Task 
(should delete task 7):
```
curl -X DELETE -u "Alex:123password123" http://127.0.0.1:8000/tasks/7/
```

# Admin Access
To access the admin interface navigate to `http://127.0.0.1:8000/admin/` and login using these credentials:
```
Username: admin
Password: 123password123
```
