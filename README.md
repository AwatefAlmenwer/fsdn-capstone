# Udacity FSDN Capstone Project
## General Specifications

Heroku Link: https://fsndp-awatef.herokuapp.com/

While running locally: http://localhost:5000

## Motivation
create full back-end using all technic we learned in this course:

- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications

## Getting Started
## Dependencies

#### 1. Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### 2. Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```

#### 3. PIP Dependencies

Once you have your virtual environment setup and running, this will install all of the required packages we selected within the `requirements.txt` file.:
```bash
pip3 install -r requirements.txt
```

#### 4. Setup Database locally
With Postgres running, restore a database using the capstone.psql file provided. From the backend folder in terminal run:
```bash
dropdb capstone 
createdb capstone
psql capstone < capstone.psql
```

#### 5. Run the Flask Application locally:
```bash
source setup.sh
python3 app.py
```

## Testing 
### For testing the backend:

```bash
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone_test.psql
source setup.sh
python3 test_app.py
```

## Authentication
 For authentication You need to setup an Auth0 account
 Note: if token is expired you can generate new token by your account in auth0 
```bash
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```
### OR 
You can Sign Up or Log In through Auth0
```bash
https://fsndp-capstone.us.auth0.com/authorize?audience=http://localhost:5000&response_type=token&client_id=uvAniqn40s8K2LJNI5iYuoxnB4BlpWlb&redirect_uri=http://localhost:8100/
```
### Roles and Permissions
#### Casting Assistant
`- All permissions a Casting Assistant has`
- GET: actors
- GET: movies

```bash
Email: assistant981276@gmail.com
Password: Assistant981276&
```

#### Casting Director

`- All permissions a Casting Director has`
- GET: actors
- GET: movies
- POST: actors
- POST: movies
- PATCH: actors
- PATCH: movies
- DELETE: actors
- DELETE: movies


```bash
Email: director98127634@gmail.com
Password: Director98127634&
```

## API Documentation
## Error Handling
The API will return three error types when requests fail:
- 400: Bad Request
Errors are returned as JSON objects in the following format:
```bash
    {
        "success": False, 
        "error": 400,
        "message": "bad request"
    }
```

- 401: Bad Request
Errors are returned as JSON objects in the following format:
```bash
    {
        "success": False, 
        "error": 401,
        "message": "unauthorized"
    }
```

- 404: Resource Not Found
Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
``` 
- 422: unprocessable
Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 422,
    "message": "unprocessable"
}
```  
## Endpoints
#### `GET /`
- General
   - main endpoint
   - is a public endpoint, requires no authentication

- Sample Request
  - `curl http://127.0.0.1:5000/`

- Sample Response
```bash
{
    "index": "Welcome to FSND capstone project!!"
}
```

#### `GET /movies`
- General
  - gets the list of all the movies
  - requires `get:movies` permission

- Sample Request
  - `curl http://127.0.0.1:5000/movies`

- Sample Response
```bash
{
    "movies": [
        {   "actors": []
            "id": 1,
            "release_year": 2016,
            "title": "La La Land"
        },
        {   
            "actors": []
            "id": 2,
            "release_year": 1997,
            "title": "Titanic"
        }
    ],
    "success": true
}
```

#### `GET /actors`
- General
  - gets the list of all the actors
  - requires `get:actors` permission

- Sample Request
  - `curl http://127.0.0.1:5000/actors`
- Sample Response 
```bash
{
    "actors": [
        {
            "age": 32,
            "gender": "F",
            "id": 1,
            "movie_id": 1,
            "name": "Emma Stone"
        },
        {
            "age": 40,
            "gender": "M",
            "id": 2,
            "movie_id": 1,
            "name": "Ryan Gosling"
        },
    {
            "age": 45,
            "gender": "M",
            "id": 3,
            "movie_id": 2,
            "name": "Leonardo DiCaprio"
        }
    
    ],
    "success": true
}
```


#### `POST /movies`
- General
  - create a new movie
  - requires `post:movies` permission

- Sample Request
```bash
curl --location --request POST 'http://localhost:5000/movies' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "title": "La La Land",
        "release_year": 2016
    }'
```
- Sample Response
```bash
{
    "created": [
        {
            "id": 1,
            "release_year": 2016,
            "title": "La La Land"
        }
    ],
    "success": true
}
```

#### `POST /actors`
- General
  - create a new movie
  - requires `post:actors` permission

- Sample Request
```bash
curl --location --request POST 'http://localhost:5000/actors' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Emma Stone",
    "gender":"F",
    "age" : 32,
    "movie_id": 1
}'
```
- Sample Response
```bash
{
    "created": [
        {
            "age": 32,
            "gender": "F",
            "id": 1,
            "movie_id": 1,
            "name": "Emma Stone"
        }
    ],
    "success": true
}
```

#### `PATCH /movies/<id>`
- General
  - Update the movie where `<id>` is the existing 
  - requires `patch:movies` permission

- Sample Request
```bash
curl --location --request PATCH 'http://localhost:5000/movies/6' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Moonlight"
    }'
``` 
- Sample Response</summary>
```bash
{
    "success": true,
    "updated": [
        {
            "id": 6,
            "release_year": 2016,
            "title": "Moonlight"
        }
    ]
}
```

#### `PATCH /actors/<id>`
- General
  - Update the actor where `<id>` is the existing 
  - requires `patch:actors` permission

- Sample Request
```bash
curl --location --request PATCH 'http://localhost:5000/actors/3' \
--header 'Content-Type: application/json' \
--data-raw '{
        "age": 46
    }'
``` 
- Sample Response</summary>
```bash
{
    "success": true,
    "updated": [
        {
            "age": 46,
            "gender": "M",
            "id": 3,
            "movie_id": 2,
            "name": "Leonardo DiCaprio"
        }
    ]
}
```   

#### `DELETE/movies/<id>`
- General
  - Delete a movie with id
  - requires `delete:movies` permission

- Sample Request
  - `curl --request DELETE 'http://localhost:5000/movies/1'`

- Sample Request  
```
{
    "deleted": 1,
    "success": true
}
```

#### `DELETE/actors/<id>`
- General
  - Delete a movie with id
  - requires `delete:actors` permission

- Sample Request
  - `curl --request DELETE 'http://localhost:5000/actors/3'`

- Sample Request  
```
{
    "deleted": 3,
    "success": true
}
```
  <br />

## Deployment
This app is deployed on Heroku. For deployment, you need to:

1. Install Heroku CLI and login to Heroku on the terminal

2. create a setup.sh file and declare all your variables in the file

3. Install gunicorn

    ```
    pip install gunicorn
    ```
4. Create a Procfile and add the line below.

    ```
    web: gunicorn app:app
    ```
5. Install the following requirements

    ```
    pip install flask_script
    pip install flask_migrate
    pip install psycopg2-binary
    ```
6. Freeze your requirements in the requirements.txt file
    ```
    pip freeze > requirements.txt
    ```
7. Create Heroku app
    ```
    heroku create name_of_your_app
    ```
8. Add git remote for Heroku to local repository
    ```
    git remote add heroku heroku_git_url
    ```
9. Add postgresql add on for our database
    ```
    heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
    ```
10. Add all the Variables in Heroku under settings
    ### This should already exist from the last step
    ```
    DATABASE_URL
    AUTH0_DOMAIN
    ALGORITHMS
    API_AUDIENCE
    ```
11. Push to Heroku
    ```
    git push heroku master
    ```
12. Run Migrations to the Heroku database
    ```
    heroku run python manage.py db upgrade --app name_of_your_application
    Visit your Heroku app on the hosted URL!
     ```


