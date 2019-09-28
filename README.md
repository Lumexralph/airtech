# AirTech

Airtech API to manage their company flight booking system. It helps to automate their processes.

## Features of the API

Provides an API that enables the user to:

- Log in
- upload passport photographs
- book tickets
- receive tickets as an email
- check the status of their flight
- make flight reservations
- purchase tickets using a payment gateway

The flight booking system also does the following:

- handle multiple requests
- optimize via caching and multi-threading


## Installing

-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```

-   Clone the airtech-api repo and cd into it:

    ```
    git clone https://github.com/Lumexralph/airtech.git

    cd airtech

-   Install dependencies to setup development environment:

    ```
    pip install virtualenv

    virtualenv venv

    source venv/bin/activate

    pip install -r requirements.txt

    ```

-   Apply migrations:

    ```
    python manage.py makemigrations

    python manage.py migrate
    ```


-   Run the application:

    ```
    python manage.py runserver
    ```


-   Should you make changes to the database models, run migrations as follows

    -   Migrate database:

        ```
        python manage.py makemigrations

        python manage.py migrate
        ```


-   Deactivate the virtual environment once you're done:
    ```
    deactivate
    ```

## Running the tests

Run the command below to run the tests for the application.
```sh
  $ python manage.py test
  ```

## API Endpoints

  Feature | Method | URL | Payload
  -------- | ------- | ------- | --------
  Create an account | POST | /auth/signup | {	"username": "name","email": "name@gmail.com","password": "name"}
  User log in | POST | /auth/login | {"email": "Sony@gmagil.com",	"password": "dayo"}
  Find a user | GET | /auth/users/{user_id}/ |
  Update user detials | PUT | /auth/users/{user_id}/ | {"username":"Sony","email":"Sony@gmagil.com","first_name": "Sony","last_name":"sunny","image_url":"image","is_admin":false} - all fields are optional
  Create flight details | POST | /flight/ | {"flight_type":"economy","to_location":"Abuja","from_location":"Lagos","departure_date":"2019-08-22","return_date":"2019-08-27","total_seats":50,"available_seats":37}
  Get all flights | GET | /flight/ |
  Find a flight | GET | /flight/{flight_id} |
  Update a flight | PUT | /flight/{flight_id} | {"flight_type":"economy","to_location":"Abuja","from_location":"Lagos","departure_date":"2019-08-22","return_date":"2019-08-27","total_seats":50,"available_seats":37} - all fields are optional
  Remove a flight | DELETE | /flight/{flight_id} |
  Create ticket for a flight | POST | /ticket/flight/{flight_id}/ | {"ticket_class":"BS","cost":0} - BS - Business
  Book a ticket for the flight | PUT | /ticket/{ticket_id}/book/ |
  Get all tickets | GET | /ticket/ |
  Get a ticket | GET | /ticket/{ticket_id} |
  Update the details of a ticket | PUT | /ticket/{ticket_id} | {"ticket_class":"BS","cost":0}
  Remove a ticket | DELETE | /ticket/{ticket_id} |
  Make reservations for a flight | PUT | /flight/{flight_id}/reservations |
  Get reservations for a flight | GET | /flight/{flight_id}/reservations |




  `After Signup or Login, a token will be  generated and can be found in the header, add this token with every request in the Authorization field (Bearer Token)`
## Deployment

The application's deployment is still pending for the backend APIs. Details will be filled here as soon as it is ready.

## Built With

The project has been built with the following technologies so far:

* [Django](https://www.djangoproject.com/) - web framework for building websites using Python
* [Django Rest Framework](https://www.django-rest-framework.org) - a powerful and flexible toolkit for building Web APIs.
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python
* [PostgreSQL](https://www.postgresql.org/) - database management system used to persists the application's data.


## Contribution guide

##### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a [Pivotal Tracker board](https://www.pivotaltracker.com/n/projects/2170023) to track the work done.

##### Pull Request Process

-   A contributor shall identify a task to be done from the [pivotal tracker](https://www.pivotaltracker.com/n/projects/2374367).If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
-   The Contributor shall then create a branch off the `develop` branch where they are expected to undertake the task they have chosen.
-   Contributors are required to activate the git pre-commit hook to auto format staged Python files to pep8 with yapf and check for residual pep8 linting errors using pylint.
    All commits are required to pass all checks from the pre-commit hook.
    The pre-commit hook can be installed as follows:
    Option 1: Copy the `hooks/pre-commit` file into the `.git/hooks` directory.
    You will need to do this every time the `hooks/pre-commit` file is changed.
    Option 2: Create a file `.git/hooks/pre-commit` then create a symlink to this file by running the command:
    `ln -s -f ../../hooks/pre-commit .git/hooks/pre-commit`
    You will only need to do this once for your local repository.
-   Although highly discouraged, the pre-commit hook can be bypassed by passing the `--no-verify` flag to the commit command as follows:
    `git commit --no-verify -m "commit message"`
-   After undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
-   If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owners of this repository.


## Copyright

Copyright (c) 2019 LumexRalph. Released under the [MIT License](https://github.com/Lumexralph/airtech/blob/develop/LICENSE).
