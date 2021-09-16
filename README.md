# IGS-Software Manager

test a implementation on heroku at: https://igs-software-manager.herokuapp.com/

By default, the project uses the [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) when open with a web browser, you can use [?format=json](https://igs-software-manager.herokuapp.com/?format=json) to view the raw json.

Written in [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/) using the [Django REST framework](https://www.django-rest-framework.org/)

## The problem

>The IGS team is growing every month and now we need to have some applications to manage employee information, such as name, e-mail and department. As any application written at IGS, It must have an API to allow integrations.

## API

The API lets you list, add and remove employees with the following fields:

Fields | Type
---|---
name | Char(30)
email | Email(256)
departament | Char(30)

## Usage

### LIST

running:
```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

returns:
```
[
    {
        "name": "Felipe Morais",
        "email": "felipe.morais@igs-software.com.br",
        "department": "Tester"
    },
    {
        "name": "Tatiane Laura",
        "email": "tatiane.laura@igs-software.com.br",
        "department": "Developer"
    },
    {
        "name": "Mauricio Alegretti",
        "email": "mauricio.alegretti@igs-software.com.br",
        "department": "RH"
}
]
```
### POST

```
curl -H "Content-Type: application/json" -X POST -d '{"name": "joejoe", "email": "joejoe@joe.com","departament": "jj"}' http://localhost:8000/employee/
```

### DELETE

```
curl -H "Accept: application/json" -X DELETE http://localhost:8000/employee/5/
```
