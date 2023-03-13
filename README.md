Todo Site
=========

This is a todo site built using Django, HTML, CSS and Bootstrap.   

I used:
* PostgreSQL - for storing, maintaining and accessing data
* Environment variables - for sensitive information
* WhiteNoise - to serve static files
* Gunicorn - takes care of everything which happens in-between the web server and web application
* Procfile and runtime.txt - to tell Railway how to run my app
* CSRF_TRUSTED_ORIGINS - A list of trusted origins
  
The site is active [here](https://todoapp-production-5d77.up.railway.app/), but not permanent due to the use of a Starter Plan in Railway.

Table of Contents
-----------------

-   [Installation](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#installation)
-   [Usage](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#usage)
-   [Features](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#features)
-   [Technologies Used](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#technologies-used)
-   [Contributing](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#contributing)
-   [License](https://github.com/AleksKostadinov/todo_app/new/main?readme=1#license)

Installation
------------

To install and run the site locally, follow these steps:

1.  Clone the repository: `git clone https://github.com/AleksKostadinov/todo_app.git`
2.  Navigate to the project directory: `cd todo_app`
3.  Install the dependencies: `pip install -r requirements.txt`
4.  Set up the database: `python manage.py migrate`
5.  Start the development server: `python manage.py runserver`
6.  Open a web browser and navigate to `http://localhost:8000/`

Usage
-----

Once the development server is running, you can use the site as follows:

1.  Register a new user account by clicking the "Register" link.
2.  Log in to your account by entering your credentials and clicking the "Login" link.
3.  Create a new todo item by filling out the form and clicking the "Add" button.
4.  Edit or delete existing todo items by clicking the "Edit" or "Delete" buttons.

Features
--------

-   User registration and authentication
-   Create, edit, and delete todo items
-   Form validation for user input

Technologies Used
-----------------

-   Django
-   HTML
-   CSS
-   Bootstrap
-   PostgreSQL

Contributing
------------

If you would like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch: `git checkout -b my-new-feature`
3.  Make changes and commit them: `git commit -am 'Add some feature'`
4.  Push to the branch: `git push origin my-new-feature`
5.  Create a pull request.

License
-------

This project is licensed under the MIT License.
