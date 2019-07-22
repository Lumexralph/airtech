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

All proposals for contribution must satisfy the guidelines in the product wiki.
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
