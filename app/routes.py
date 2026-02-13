from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from app.models import Cliente
from app import db

main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():
    return render_template("index.html")


@main.route("/clientes")
@login_required
def listar_clientes():
    if current_user.rol != "admin":
        abort(403)

    clientes = Cliente.query.all()
    return render_template("clientes/lista.html", clientes=clientes)


@main.route("/clientes/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_cliente():
    if current_user.rol != "admin":
        abort(403)

    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        telefono = request.form["telefono"]

        nuevo = Cliente(
            nombre=nombre,
            email=email,
            telefono=telefono
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for("main.listar_clientes"))

    return render_template("clientes/nuevo.html")


@main.route("/clientes/<int:id>/editar", methods=["GET", "POST"])
@login_required
def editar_cliente(id):
    if current_user.rol != "admin":
        abort(403)

    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":
        cliente.nombre = request.form["nombre"]
        cliente.email = request.form["email"]
        cliente.telefono = request.form["telefono"]

        db.session.commit()
        return redirect(url_for("main.listar_clientes"))

    return render_template("clientes/editar.html", cliente=cliente)


@main.route("/clientes/<int:id>/eliminar", methods=["POST"])
@login_required
def eliminar_cliente(id):
    if current_user.rol != "admin":
        abort(403)

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for("main.listar_clientes"))
