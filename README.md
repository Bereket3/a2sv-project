##installiation

1. create virtual environmnet and install all liberaries in the requirement.txt
2. activate your virtual environment
3. run the command py manage.py runserver

## Testing

1. the default host will be https://localhost:8000
2. go to postman or other api testers and your host will be https://localhost:8000
3. endpoints are:

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

## programing language and framework
programing language -> python
framework -> Django, Django-rest-framework

## Name and email

Name: Bereket Worku
E-mail: bereker.worku@a2sv.org
   
    