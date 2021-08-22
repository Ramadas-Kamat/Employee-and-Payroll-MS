# Employee and Payroll Management System

The project aims at creating a payroll management system for micro and small scale industries. The web application is built using Python's Django framework, with an elegant Bootstrap based front end. 





## Features

- Management of Employee attendance and salary
- Deductions and overtime benefits automatically based on attendance
- Generation of salary slip 



This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech used

The system makes use of the following technology:

1. [Django](https://www.djangoproject.com), the project is built with Python based Django framework.
2. [Bootstrap](https://getbootstrap.com) is used for the frontend. The [Softland](https://bootstrapmade.com/softland-bootstrap-app-landing-page-template/) bootstrap template is used in this project.
3. [MySQL](https://mysql.com) database is used in deployment.
4. HTML, CSS and Javascript for web page design.



## Installation
The system needs to have Python 3.6 or higher installed.
Follow these instructions for installation,



```sh
git clone https://github.com/Ramadas-Kamat/Employee-and-Payroll-MS
cd Employee-and-Payroll-MS
```

The requirements for the project can be installed using

```sh
pip install -r requirements.txt
```

Django comes with sqlite database by default, to change the database modify the settings.py file.

The django models can be imported to the connected database by running

```
python manage.py makemigrations
python manage.py migrate
```

To get the static files for the frontend run,

```sh
python manage.py collectstatic
```
To run the project

```sh
python manage.py runserver
```

## License
MIT
