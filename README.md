# Overview
This app lets groups or families create tasks and categories, assign tasks to members, and mark them as completed. Built for an interview task, it simplifies managing group chores and activities.
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
- List Users:
```
curl http://127.0.0.1:8000/users/
```
- Get Task Details:
```
curl http://127.0.0.1:8000/tasks/1/
```
- Create Task (with wrong Auth - it should fail):
```
curl -X POST -u "Alex:123password1231" -H 'Content-Type: application/json' -d '{"title": "Vacuum living room", "description": "Vacuum the entire living room.", "category":1, "assigned_to":4}' http://127.0.0.1:8000/tasks/
```
- Create Task (with Auth):
```
curl -X POST -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"title": "Vacuum living room", "description": "Vacuum the entire living room.", "category":1, "assigned_to":4}' http://127.0.0.1:8000/tasks/
```
- Modify Task (PUT):
```
curl -X PUT -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"title": "Clean window", "description": "Clean all windows on the upper floor.", "category":1, "completed":"True"}' http://127.0.0.1:8000/tasks/1/
```
- Update Task (PATCH):
```
curl -X PATCH -u "Alex:123password123" -H 'Content-Type: application/json' -d '{"assigned_to":1}' http://127.0.0.1:8000/tasks/1/
```
- Delete Task:
```
curl -X DELETE -u "Alex:123password123" http://127.0.0.1:8000/tasks/7/
```

# Admin Access
To access the admin interface navigate to `http://127.0.0.1:8000/admin/` and login using these credentials:
```
Username: admin
Password: 123password123
```
