<div align="center">
<h1><a href="https://task-manager-52.up.railway.app/">Task manager</h1>
<p>Task Manager is a task management system. It allows you to set tasks, assign performers and change their statuses. To work with the system registration and authentication are required.</p>
<p>Follow the following link to try: <a href="https://task-manager-52.up.railway.app/">Task manager</a></p>

[![Actions Status](https://github.com/KsyushaKI/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/KsyushaKI/Task-manager/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7024875e757c3364021a/maintainability)](https://codeclimate.com/github/KsyushaKI/Task-manager/maintainability)

</div>


## About

A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

To provide users with a convenient, adaptive, modern interface, the project uses the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

[Website](https://task-manager-52.up.railway.app/)

### Features

* [x] Set tasks;
* [x] Assign performers;
* [x] Change task statuses;
* [x] Set multiple tasks labels;
* [x] Filter the tasks displayed;
* [x] User authentication and registration;

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Poetry](https://python-poetry.org/)
* [Gunicorn](https://gunicorn.org/)
* [Rollbar](https://rollbar.com/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

### Details

For **_user_** authentication, the standard Django tools are used. In this project, users will be authorized for all actions, that is, everything is available to everyone.

Each task in the task manager usually has a **_status_**. With its help you can understand what is happening to the task, whether it is done or not. Tasks can be, for example, in the following statuses: _new, in progress, in testing, completed_.

**_Tasks_** are the main entity in any task manager. A task consists of a name and a description. Each task can have a person to whom it is assigned. It is assumed that this person performs the task. Also, each task has mandatory fields - author (set automatically when creating the task) and status.

**_Labels_** are a flexible alternative to categories. They allow you to group the tasks by different characteristics, such as bugs, features, and so on. Labels are related to the task of relating many to many.

When the tasks become numerous, it becomes difficult to navigate through them. For this purpose, a **_filtering mechanism_** has been implemented, which has the ability to filter tasks by status, performer, label presence, and has the ability to display tasks whose author is the current user.

### Available Actions:

- **_Registration_** — First, you need to register in the application using the registration form provided;
- **_Authentication_** — To view the list of tasks and create new ones, you need to log in using the information from the registration form;
- **_Users_** — You can see the list of all registered users on the corresponding page. It is available without authorization. You can change or delete information only about yourself. If a user is the author or performer of a task, it cannot be deleted;
- **_Statuses_** — You can view, add, update, and delete task statuses if you are logged in. Statuses corresponding to any tasks cannot be deleted;
- **_Tasks_** — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
- **_Labels_** — You can view, add, update, and delete task labels if you are logged in. Labels matching any tasks cannot be deleted.

### Dependencies

* python = ">=3.10"
* Django = "^4.2.2"
* psycopg2-binary = "^2.9.6"
* python-dotenv = "^1.0.0"
* dj-database-url = "^2.0.0"
* gunicorn = "^20.1.0"
* django-bootstrap4 = "^23.1"
* django-filter = "^23.2"
* rollbar = "^0.16.3"

This is the fourth and **final** training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@KsyushaKI](https://github.com/KsyushaKI) &nbsp;&middot;&nbsp;
> LinkedIn [@Oksana Karshakevich](https://www.linkedin.com/in/oksana-karshakevich-097663243/)
