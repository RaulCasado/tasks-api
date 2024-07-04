  Flask Tasks API

Flask Tasks API
===============

Description
-----------

This project implements a RESTful API using Flask to manage user tasks. The API allows users to register, log in, manage their tasks, and perform basic CRUD operations on them. Authentication is handled using JWT (JSON Web Tokens) to secure protected routes.

Environment Setup
-----------------

1.  **Clone the repository:**  
    `git clone https://github.com/RaulCasado/tasks-api.git`
2.  **Install dependencies:**  
    `pip install -r requirements.txt`
3.  **Set up the database:**  
    *   Create a PostgreSQL database (or another compatible engine).
    *   Configure environment variables or the `config.py` file with database credentials.
4.  **Configure environment variables:**  
    *   Create a `.env` file in the project root and define necessary environment variables (e.g., `DATABASE_URL`, `JWT_SECRET_KEY`, etc.).

Running the Project
-------------------

1.  **Activate the virtual environment (optional but recommended):**  
    `source venv/bin/activate`
2.  **Start the application:**  
    `flask run`
3.  The application will be available at `http://localhost:5000`.

Using the API
-------------

### Available Endpoints

*   **GET /api/tasks**: Get all tasks.(requires JWT authentication).
*   **GET /api/tasks/{task\_id}**: Get details of a specific task.(requires JWT authentication).
*   **POST /api/tasks**: Create a new task (requires JWT authentication).
*   **PUT /api/tasks/{task\_id}**: Update an existing task (requires JWT authentication).
*   **DELETE /api/tasks/{task\_id}**: Delete an existing task (requires JWT authentication).
*   **GET /api/users**: Get all users.
*   **GET /api/users/{user\_id}**: Get details of a specific user.
*   **POST /api/users**: Register a new user.
*   **PUT /api/users/{user\_id}**: Update an existing user's information (requires JWT authentication).
*   **DELETE /api/users/{user\_id}**: Delete an existing user (requires JWT authentication).
*   **POST /api/login**: Log in and obtain a JWT token.
*   **POST /api/register**: Register a new user in the system.

### Authentication

To perform operations that require JWT authentication (create, update, or delete tasks and users), include the JWT token in the HTTP request header as follows:

    Authorization: Bearer {your_jwt_token}

Replace `{your_jwt_token}` with the valid JWT token obtained upon logging in. If you use Postman you can just add the token to Authentification and select Bearer.

Examples
--------

### Example of a POST request to create a task

    POST /api/tasks
    
        {
          "title": "New Task",
          "description": "Description of the new task",
          "status": "pending",
          "user_id": 3,
          "tags": [1, 2],
          "categories": [1]
        }

### Example of a PUT request to update a task

    PUT /api/tasks/7
    
        {
          "title": "Updated Task",
          "status": "in_progress"
        }
