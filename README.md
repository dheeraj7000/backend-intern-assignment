# backend-project
The Task Manager API is a simple web service built with Flask that allows users to manage tasks. It 
provides endpoints for creating, reading, updating, and deleting tasks stored in a SQLite database. 
This README will guide you on how to test the project and install the required dependencies.

Getting Started

Clone the Repository

Clone this repository to your local machine using the following command:

bash : 
git clone https://github.com/your-username/task-manager-api.git
Navigate to the Project Directory

Change your current working directory to the project folder:

bash : 
cd backend-assignment-intern
Install Dependencies

The API requires some Python dependencies, which you can install using pip. 
It is recommended to set up a virtual environment before installing dependencies:

bash : 
python -m venv venv
source venv/bin/activate  # On Windows, use: ->venv\Scripts\activate
pip install -r requirements.txt
Create Database and Run the Server

Before running the application, create the SQLite database and start the server:
->python app.py
The server should be up and running at http://localhost:5000/.

Testing the API :
The API can be tested using a tool like curl, Postman, or any other HTTP client. 

Below are some sample requests for testing:

Create a new task : 

vbnet : 
curl -X POST -H "Content-Type: application/json" -d '{
    "title": "Finish Report",
    "description": "Complete the quarterly report",
    "due_date": "2023-07-31",
    "status": "Incomplete"
}' http://localhost:5000/tasks
Retrieve a single task

bash : 
curl http://localhost:5000/tasks/<task_id>
Update an existing task

vbnet : 
curl -X PUT -H "Content-Type: application/json" -d '{
    "title": "Finish Report",
    "description": "Complete the quarterly report",
    "due_date": "2023-08-15",
    "status": "Completed"
}' http://localhost:5000/tasks/<task_id>
Delete a task

bash : 
curl -X DELETE http://localhost:5000/tasks/<task_id>
List all tasks (with pagination)

bash : 
curl http://localhost:5000/tasks?page=1&per_page=5
API Error Handling

The API provides error handling for scenarios where tasks are not found (404 status) and when invalid data is provided (400 status).

Contributing : If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request. Contributions are welcome!

License : This project is licensed under the MIT License. See the LICENSE file for details.

Happy coding!
