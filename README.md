# : Backend Development
## Project Description : hi

Task 1 focuses on creating a Python-based API for managing app details. The API provides endpoints to perform basic
CRD operations (Create, Read, and Delete) on app data. It is designed to be RESTful, lightweight, and easily 
deployable, with Docker used to simplify setup and deployment. The endpoints allow users to add app details,
retrieve specific app information by ID, and delete apps by ID.

## Features :
1. POST /add-app:
      Purpose: Adds new app details to the database.
      Request: Accepts JSON data with fields app_name, version, and description.
      Response: Returns a success message with the app's ID.(Remember That id for further works)

2. GET /get-app/{id}:
      Purpose: Retrieves details of an app by its unique ID.
      Request: Requires an id parameter (e.g., /get-app/1).
      Response: Returns the app’s app_name, version, and description.

3. DELETE /delete-app/{id}:
      Purpose: Deletes an app by its ID.
      Request: Requires an id parameter (e.g., /delete-app/1).
      Response: Returns a success message confirming the deletion.

## Installation Instructions :
  ### Prerequisites :
    docker
    docker-compose
  ### Steps :
  #### 1. Go to the project directory : 
          cd Api_assignment
  #### 2. Start the container : 
          docker-compose up --build
## Usage : 
  Access The API Application :
      Once the Docker containers are up and running, you can access the Django application at-
      http://localhost:8000


# : Database Management
## Project Description :

Focuses on setting up and managing a PostgreSQL database to store app details (app_name, version, description). The database is integrated with the Django API from Task 1, using Docker to provide a consistent development and production environment. PostgreSQL is used as the primary database, ensuring scalability and reliability. Migrations handle schema creation and updates.

## Features :
1. Database: PostgreSQL managed via Docker.
2. Integration: Seamless integration with the Django API.
3. Data Management: Efficient management of app details with migration support.

## Schema File :
  test_api\migrations\0001_initial.py

## Data for API Testing :
  [  {
        "app_name": "App One",
        "version": "1.0",
        "description": "This is the first app."
        }
    ,
    {
        "app_name": "App Two",
        "version": "2.3",
        "description": "An updated version of the second app."
    }
    ,
    {
        "app_name": "App Three",
        "version": "1.5.1",
        "description": "Bug fixes and performance improvements."
    }
    ,
    {
        "app_name": "App four",
        "version": "1.1",
        "description": "Update Scalability."
    }
  ]
## Note : 
Use the provided list of JSON formatted datas separately for testing the API.



