python -m venv ll_env

powershell admin this is required to run scripts 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

once the venv is activated then 
pip install django

a certain version may be required
pip install django==2.2.*.

django-admin startproject learning_log .

within application root folder create a database 
python manage.py migrate

once the server is running connect to the venv using a new terminal and
python manage.py startapp learning_logs

enter a django shell
python manage.py shell

run the server
python manage.py runserver

activate the virtual environment
ll_env/Scripts/activate