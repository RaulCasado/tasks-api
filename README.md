Flask Tasks API
===============

The **Flask Tasks API** is a RESTful API for managing user tasks. It allows users to register, log in, and perform CRUD operations on tasks. Authentication is secured using **JWT (JSON Web Tokens)**, ensuring protected routes are only accessible to authorized users.

Features
--------

*   **User Authentication:** Register and log in users with secure password hashing.
*   **JWT-based Authentication:** Secure access to protected endpoints.
*   **Task Management:** Create, retrieve, update, and delete tasks.
*   **CRUD Operations:** Manage users and tasks efficiently.
*   **Dockerized:** No need to install Python or MySQL locally.

Environment Setup
-----------------

### Prerequisites

*   Docker and Docker Compose must be installed on your machine.

### Steps to Set Up

1.  **Clone the Repository:**
    
    git clone https://github.com/RaulCasado/tasks-api.git  
    cd tasks-api
    
2.  **Create a .env File:** Configure environment variables in the root `.env` file for database and JWT secrets.
3.  **Example .env File:**
    
    MYSQL\_ROOT\_PASSWORD=root\_password
    MYSQL\_DATABASE=app\_database
    MYSQL\_USER=app\_user
    MYSQL\_PASSWORD=app\_password
    JWT\_SECRET\_KEY=your\_secret\_key
                
    
4.  **Build and Start the Application:**
    
    sudo docker compose --env-file .env up --build
    
5.  **Access the API:** `http://localhost:5000`

API Endpoints
-------------

### User Endpoints

*   `POST /api/register`: Register a new user.
*   `POST /api/login`: Log in and obtain a JWT token.
*   `GET /api/users`: Get all users.
*   `GET /api/users/{user_id}`: Get details of a specific user.
*   `PUT /api/users/{user_id}`: Update user information.
*   `DELETE /api/users/{user_id}`: Delete an existing user.

### Task Endpoints

*   `GET /api/tasks`: Get all tasks for the current user.
*   `GET /api/tasks/{task_id}`: Get details of a specific task.
*   `POST /api/tasks`: Create a new task.
*   `PUT /api/tasks/{task_id}`: Update an existing task.
*   `DELETE /api/tasks/{task_id}`: Delete an existing task.

Examples
--------

### Register a User

curl -X POST http://localhost:5000/api/register \\
-H "Content-Type: application/json" \\
-d '{
  "username": "new\_user",
  "email": "new\_user@example.com",
  "password": "securepassword"
}'
    

### Log In a User

curl -X POST http://localhost:5000/api/login \\
-H "Content-Type: application/json" \\
-d '{
  "email": "new\_user@example.com",
  "password": "securepassword"
}'
    

### Create a Task

curl -X POST http://localhost:5000/api/tasks \\
-H "Authorization: Bearer {your\_jwt\_token}" \\
-H "Content-Type: application/json" \\
-d '{
  "title": "Test Task",
  "description": "Testing task creation",
  "status": "pending",
  "categories": \[1\],
  "tags": \[2\]
}'
    

### Update a Task

curl -X PUT http://localhost:5000/api/tasks/1 \\
-H "Authorization: Bearer {your\_jwt\_token}" \\
-H "Content-Type: application/json" \\
-d '{
  "title": "Updated Task",
  "status": "in\_progress"
}'
    

### Delete a Task

curl -X DELETE http://localhost:5000/api/tasks/1 \\
-H "Authorization: Bearer {your\_jwt\_token}"
    

