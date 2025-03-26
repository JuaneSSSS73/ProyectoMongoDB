## 📝 Formulario con MySQL
## 📖 Descripción del Proyecto
Este proyecto fue desarrollado en la Clase de Git y GitHub del profesor Juan Pablo Jiménez, donde se nos pedía desarrollar un CRUD con una base de datos de MySQL, que realizamos en la clase de Base de Datos del profesor Christian Gámez.
El propósito de este proyecto es poner en práctica los conocimientos adquiridos en Git y GitHub, como:

-Subir archivos a un repositorio de GitHub utilizando Git Bash.
-Clonar repositorios.
-Realizar commits bien estructurados que nos ayudarán en el futuro.

Además, aplicamos los conocimientos adquiridos en bases de datos, diseñando y gestionando una base de datos relacional con MySQL.

## ✅ Pre-requisitos
### 🚀 Tecnologías utilizadas

Python Lenguaje de programación principal
Flask Framework web en Python
MySQL Base de datos relacional
MySQL Connector Librería para conectar Python con MySQL
Bootstrap Para mejorar el diseño del formulario

### 🖥️ Software necesario:
Python 3.13.2
MySQL Server ejecutándose en localhost
Git Bash

### 📦 Instalación de dependencias:
Ejecutar el siguiente comando para instalar las dependencias necesarias:
bash
Copy
Edit
pip install -r requirements.txt

## 📂 Estructura del Proyecto
📦 FormularioMySQL  
 ┣ 📂 src/
 ┣ ┣📂 templates/
   ┃ ┣ 📜 editar.html  
   ┃ ┣ 📜 index.html  
 ┣ 📜 app.py  
 ┣ 📂 __pycache__
 ┣ ┣ 📜 database.cpython
 
## 🗄️Modelo de Base de Datos (MySQL)
La base de datos en MySQL almacena la información de los usuarios en la siguiente estructura:
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    numero VARCHAR(20) NOT NULL
);
Ejemplo de datos en la tabla:

id	Nombre	Email	Número
1	Juan Pérez	juan@gmail.com	3156789123
2	María López	maria@gmail.com	3145678901

## ✨ Funcionalidades
### 1️⃣ Inicio y visualización de usuarios
La página index.html muestra una lista de usuarios registrados en la base de datos MySQL.
Se genera una tabla para visualizar los datos, con opciones para editar o eliminar usuarios.

<table class="table table-bordered table-striped mt-3">
    <thead class="table-dark">
        <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Número</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for usuario in usuarios %}
        <tr>
            <td>{{ usuario[1] }}</td>
            <td>{{ usuario[2] }}</td>
            <td>{{ usuario[3] }}</td>
            <td>
                <a href="{{ url_for('editar', id=usuario[0]) }}" class="btn btn-warning btn-sm">Editar</a>
                <a href="{{ url_for('eliminar', id=usuario[0]) }}" class="btn btn-danger btn-sm" onclick="return confirm('¿Seguro que quieres eliminar este usuario?')">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

### 2️⃣Agregar un usuario
El archivo index.html permite ingresar nombre, email y número de teléfono de un usuario y almacenarlo en MySQL.

<form action="/agregar" method="post">
    <div class="mb-3">
        <label for="nombre" class="form-label">Nombre:</label>
        <input type="text" class="form-control" name="nombre" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="email" class="form-control" name="email" required>
    </div>
    <div class="mb-3">
        <label for="numero" class="form-label">Número:</label>
        <input type="text" class="form-control" name="numero" required>
    </div>
    <button type="submit" class="btn btn-primary">Guardar</button>
</form>

### 3️⃣ Editar un usuario
Permite actualizar la información de un usuario existente.

<form action="{{ url_for('editar', id=usuario[0]) }}" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" value="{{ usuario[1] }}" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="{{ usuario[2] }}" required>
    <br>
    <label for="numero">Número:</label>
    <input type="text" id="numero" name="numero" value="{{ usuario[3] }}" required>
    <br>
    <button type="submit">Actualizar</button>
</form>

### 4️⃣Eliminar un usuario
Permite eliminar un usuario de la base de datos.

<a href="{{ url_for('eliminar', id=usuario[0]) }}" class="btn btn-danger btn-sm" onclick="return confirm('¿Seguro que quieres eliminar este usuario?')">Eliminar</a>

## 5️⃣ Código en app.py
Este archivo maneja la lógica de la aplicación:
Se conecta a la base de datos MySQL.
Define las rutas para listar, agregar, editar y eliminar usuarios.
Ejecuta Flask en modo debug para facilitar el desarrollo.

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)
cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return render_template("index.html", usuarios=usuarios)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    numero = request.form.get("numero")

    cursor.execute("INSERT INTO usuarios (nombre, email, numero) VALUES (%s, %s, %s)", (nombre, email, numero))
    db.commit()
    
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for("index"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        numero = request.form.get("numero")

        cursor.execute("UPDATE usuarios SET nombre=%s, email=%s, numero=%s WHERE id=%s", (nombre, email, numero, id))
        db.commit()
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    return render_template("editar.html", usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)
## 📌 Versión
Branch principal: master
Branch actuak: FormularioMySQl
Base de datos: MySQL

## 👨‍💻 Desarrollado por
📌 Juan Esteban Montoya Cadavid
✉️ Contacto: juanesalv443@gmail.com
