from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1022114520",
    database="biblioteca"
)
cursor = database.cursor()

@app.route('/')
def home():
    cursor = database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    cursor.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    email = request.form['email']
    numero = request.form['numero']  # Cambiado de telefono a numero

    cursor = database.cursor()
    sql = "INSERT INTO usuario (nombre, email, numero) VALUES (%s, %s, %s)"
    valores = (nombre, email, numero)
    cursor.execute(sql, valores)
    database.commit()
    return redirect(url_for('home'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursor = database.cursor()
    sql = "DELETE FROM usuario WHERE id=%s"
    cursor.execute(sql, (id,))
    database.commit()
    return redirect(url_for('home'))

@app.route('/editar/<int:id>')
def editar(id):
    cursor = database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    return render_template('editar.html', usuario=usuario)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    nombre = request.form['nombre']
    email = request.form['email']
    numero = request.form['numero']  # Cambiado de telefono a numero

    cursor = database.cursor()
    sql = "UPDATE usuario SET nombre=%s, email=%s, numero=%s WHERE id=%s"
    valores = (nombre, email, numero, id)
    cursor.execute(sql, valores)
    database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
