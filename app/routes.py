from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Cliente
from app import db

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/clientes")
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template("clientes/lista.html", clientes=clientes)

@main.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        objetivo = request.form["objetivo"]
        estado = request.form["estado"]

        nuevo = Cliente(
            nombre=nombre,
            email=email,
            telefono=telefono,
            objetivo=objetivo,
            estado=estado
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for("main.listar_clientes"))

    return render_template("clientes/nuevo.html")

@main.route("/clientes/<int:id>/editar", methods=["GET", "POST"])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":
        cliente.nombre = request.form["nombre"]
        cliente.email = request.form["email"]
        cliente.telefono = request.form["telefono"]
        cliente.objetivo = request.form["objetivo"]
        cliente.estado = request.form["estado"]

        db.session.commit()
        return redirect(url_for("main.listar_clientes"))

    return render_template("clientes/editar.html", cliente=cliente)

@main.route("/clientes/<int:id>/eliminar", methods=["POST"])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for("main.listar_clientes"))
