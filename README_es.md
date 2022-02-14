# Ejemplo práctico de API rest con Python, Flask, SQLAlchemy y SQLite

## Ejercicio básico de un crud con Python

Este ejercicio es un ejemplo básico de un crud con *Python, flask y SQLite*, es un **API** para guardar, consultar, actualizar, y eliminar una lista de usuarios, el objetivo de esta **API** será convertirse en un servicio de ***Fake users generator***, actualmente solo se cuentan con 3 endpoints para los métodos, *GET*, *POST*, *PUT*

### Instalar el proyecto

Para instalar el proyecto después de clonarlo debes iniciar un entorno virtual en el cual deberás agregar todas las instalaciones necesarias y, obviamente, tener instalado Python 3

### Dependencias

Las dependencias que se necesitaran instalar para ejecutar correctamente la aplicación son: 
- flask
- flask-sqlalchemy
- flask-marshmallow
- marshmallow-sqlalchemy

como base de datos se usará SQLite el cual ya viene en los paquetes de Python por lo que no hay que instalar nada más

El comando para instalar todas las dependencias con pip será

~~~
pip install flask flask-sqlalchemy flask-marshmallow masrshmallow-sqlalchemy
~~~

### Arrancar el app

Para correr el app, una vez instalado todas las dependencias, ejecuta el siguiente comando desde la carpeta del proyecto

~~~
 pyhton3 app.py
~~~

Esto ejecuta la app en el ***localhost:5000***

### Agregar un usuario

Para agregar un usuario se debe enviar un objeto JSON al siguiente endpoint atrevés del método *POST*

~~~
/user
~~~

el objeto deberá contener lo siguiente:

~~~
{
    "name": "string",
    "additionalName": "string",
    "lastName": "string",
    "secondLastName": "string",
    "age": 0,
    "birthDate": "string"
}
~~~

### Consultar los usuarios existentes

Para consultar los usuarios existentes se debe hace una petición *GET* al siguiente endpoint:

~~~
/users
~~~

El cual responderá con una lista de usuarios en el siguiente formato

~~~
[
    {
        "name": "string",
        "additionalName": "string",
        "lastName": "string",
        "secondLastName": "string",
        "age": 0,
        "birthDate": "string"
    }
]
~~~

### Consultar un único usuario

Para consultar un único usuario se debe hacer una petición *GET* al siguiente endpoint: 

~~~
/user/{id}
~~~

Donde ***{id}*** se remplaza por el ID del usuario a consultar

### Actualizar un usuario

Para actualizar un usuario se debe hacer una petición *PUT* al siguiente endponit:

~~~
/user/{id}
~~~

Donde ***{id}*** se remplaza por el ID del usuario a actualizar adicionalmente se debe enviar un objeto JSON con los nuevos datos de usuario en el siguiente formato:

~~~
{
    "name": "string",
    "additionalName": "string",
    "lastName": "string",
    "secondLastName": "string",
    "age": 0,
    "birthDate": "string"
}
~~~