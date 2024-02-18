## Installiation

1. Create virtual environmnet and install all liberaries in the requirement.txt
   Commands:
      1. py -m venv venv
      2. To activate the virtual environment
         -> on cmd venv\scripts\activate.bat
         -> on powershell venv/scripts/Activate.ps1
         -> on git bash cd venv/scripts and . activate
      3. pip install -r requirement.txt

2. Activate your virtual environment
3. run the command py manage.py makemigrations
4. run the command py manage.py migrate
4. run the command py manage.py runserver

## Testing

1. By default host will be https://localhost:8000
2. Go to postman or other api testers and your host will be https://localhost:8000
3. Endpoints are:

       1. https://localhost:8000/tasks -> method GET
          * description:
               -> list all the tasks in the database
   
       2. https://localhost:8000/tasks -> method POST
          * description:
               -> create a new task
   
       3. https://localhost:8000/tasks/{id} -> method GET
          * description:
               -> get a task from database with id
   
       4. https://localhost:8000/tasks/{id} -> method PUT
          * description:
               -> update a task by its id
   
       5. https://localhost:8000/tasks/{id} -> method DELETE
          * description:
               -> delete a task by it's id

## Programing language, Framework and Database
1. Programing language -> python
2. Framework -> Django, Django-rest-framework
3. Database Mysql

## Name and email
1. Name: Bereket Worku
2. E-mail: bereker.worku@a2sv.org