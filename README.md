Installation Instructions

1. Make sure you install python 3.0 and above

2. Create a project environment, run PowerShell:
> mkdir myproject
> cd myproject
> py -3 -m venv .venv

3. Activate the environment:
> .venv\Scripts\activate

4. Install flask
> pip install Flask

5. Install mysqldb:
> pip install flask-mysqldb

6. Install dotenv:
> pip install python-dotenv


To run flask, execute this command:
> flask --app main run --debug