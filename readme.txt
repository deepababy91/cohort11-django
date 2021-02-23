mkdir cohort11a
cd cohort11a
pipenv install --python 3
pipenv install django
pipenv shell
django-admin startproject config .
python manage.py runserver
python manage.py migrate
python manage.py startapp pages
follow https://djangoforbeginners.com/hello-world/ tutorial
