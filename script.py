from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]
collection = db["usuarios"]

@app.route("/")
def index():
    usuarios = collection.find()
    return render_template("index.html", usuarios=usuarios)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    numero = request.form.get("numero")

    if nombre and email and numero:
        collection.insert_one({"nombre": nombre, "email": email, "numero": numero})
    
    return redirect(url_for("index"))

@app.route("/eliminar/<id>")
def eliminar(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        numero = request.form.get("numero")

        if nombre and email and numero:
            collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nombre": nombre, "email": email, "numero": numero}}
            )
        return redirect(url_for("index"))
    
    usuario = collection.find_one({"_id": ObjectId(id)})
    return render_template("editar.html", usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)
