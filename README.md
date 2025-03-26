# # 📝 Formulario con MongoDB

## 📖 Descripción del Proyecto
Este proyecto fue desarrollado en la Clase de Git y GitHub del profesor Juan Pablo Jiménez, donde se nos pedía desarrollar un CRUD con una base de datos de MongoDB,
que realizamos en la clase de Base de datos del profesor Christian Gámez. Este proyecto fue con el objetivo de aprender y aplicar los conocimientos que adquirimos
en las otras clases. El propósito de este proyecto fue poner en práctica los conocimientos de Git y GitHub como subir archivos a un repositorio de GitHub utilizando
Git Bash, además de aprender de a clonar repositorios y hacer commits bien estructurados que nos van ayudar para el futuro.

## ✅ Pre-requisitos

### 🚀 Tecnologías utilizadas

Python Lenguaje de programación para hacer la conexión de base de datos con el templates
Flask Framework web en Python
MongoDB Base de datos NoSQL
PyMongo Librería para conectar Python con MongoDB
Bootstrap Para mejorar el diseño del formulario

### 🖥️ Software necesario:
- Python 3.13.2
- MongoDB ejecutándose en `localhost:27017`
- Git Bash

### 📦 Instalación de dependencias:
Hay paquetes necesarios para realizar este proyecto tales como:

`bash pip install -r requirements.txt`

## 📂 Estructura del proyecto
📦 FormularioMongoDB  
   ┣ 📂 templates/  
   ┣ 📜 editar.html
   ┣ 📜 index.html
 ┣ 📜 script.py

## 🗄️ Modelo de Base de Datos (MongoDB)
La base de datos en MongoDB almacena la información de los documentos con la siguiente estructura:
{"_id":{"$oid":"67bfcd4bf8b1b87b4646b558"},"nombre":"Abuela Coco","email":"abuelacoco@gmail.com","numero":3.126714981E+09}
{"_id":{"$oid":"67bfcd4bf8b1b87b4646b559"},"nombre":"Thanos Escobar Gaviria","email":"thanos123@gmail.com","numero":3.153458791E+09}

## ✨ Funcionalidades
### 1️⃣ Inicio y visualización de usuarios
La pagina de index.html muestra una lista de usuarios registrados en la base de datos MongoDb. Se realiza una tabla para visualizar los datos, con opciones para editar
o eliminar usuarios
<table class="table table-bordered table-striped mt-3">
    <thead class="table-dark">
        <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Número</th>
        </tr>
    </thead>
    <tbody>
        {% for usuario in usuarios %}
        <tr>
            <td>{{ usuario.nombre }}</td>
            <td>{{ usuario.email }}</td>
            <td>{{ usuario.numero }}</td>
            <td>
                <a href="{{ url_for('editar', id=usuario._id) }}" class="btn btn-warning btn-sm">Editar</a>
                <a href="{{ url_for('eliminar', id=usuario._id) }}" class="btn btn-danger btn-sm" onclick="return confirm('¿Seguro que quieres eliminar este usuario?')">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
### 2️⃣ Agregar un usuario
El archivo de index.html permite ingrear nombre, email y numero de teléfono de un usuario y almacernarlo en MongoDB
<form action="/agregar" method="post">
    <div class="mb-3">
        <label for="nombre" class="form-label">Nombre:</label>
        <input type="text" class="form-control" name="nombre" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="email" class="form-control" name="email" required>
    </div
    <div class="mb-3">
        <label for="numero" class="form-label">Número:</label>
        <input type="text" class="form-control" name="numero" required>
    </div>
    <button type="submit" class="btn btn-primary">Guardar</button>
</form>

### 3️⃣ Editar un usuario
Permite actualizar la información de un usuario existente. El formulario carga en la página los datos que ingresamos anteriormente y permite modificarlos
<form action="{{ url_for('editar', id=usuario._id) }}" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" value="{{ usuario.nombre }}" required>
    <br
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="{{ usuario.email }}" required>
    <br>
    <label for="numero">Número:</label>
    <input type="text" id="numero" name="numero" value="{{ usuario.numero }}" required>
    <br>
    <button type="submit">Actualizar</button>
</form>

### 4️⃣ Eliminar un usuario
Permite eliminar un usurio mediante un botón de eliminar con un mensaje de confirmación.
<a href="{{ url_for('eliminar', id=usuario._id) }}" class="btn btn-danger btn-sm" onclick="return confirm('¿Seguro que quieres eliminar este usuario?')">Eliminar</a>

### 5️⃣ Script.py
El archivo script.py es el corazón de la aplicación. se encarga de manejar las rutas, conectarse con la base de datos y ejecutar las operaciones CRUD en MongoDB.
El archivo importa líbrerias para desarrollador toda la aplicación por ejemplo Flask que maneja toda la lógica web, PyMongo para conectarse a MongoDb y ObjectId
para gestionar los identificadores únicos de MongoDb, además define las rutas principales por ejemplo /agregar, /editar/<id> Y eliminar/<id>.
Para ejecutarlo se utiliza el servidor Flask en modo debug, lo que facilita la detección de errores.

## 📌 Versión
- Branch principal: Master
-Base de datos: MongoDB

👨‍💻 Desarrollado por
📌 Juan Esteban Montoya Cadavid
✉️ Contacto: juanesalv443@gmail.com


