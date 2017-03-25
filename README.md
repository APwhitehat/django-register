# django-register
Mini web server for user registration on postgreSQL (made with help of Django)

This was made to test/demonstrate remote user registration on postgreSQL .
I intend to use this to authenticate user in realtime.

### How to use

<ul>
	<li>Install and setup postgreSQL</li>
	<li>Make a database named <code>newdb</code> (Owner = postgres_user) or change setting.py DATABASE info</li>
	<li>git clone this repo</li>
	<li>Setup virtualenv as per your need</li>
	<li>Install django</li>
	<li>Run <code>python manage.py runserver</code> </li>
</ul>

You may need to run

`python manage.py makemigrations` &

`python manage.py migrate`

to setup database migrations before `runserver`
