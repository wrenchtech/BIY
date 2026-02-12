from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Client
from ..extensions import db

clients = Blueprint("clients", __name__, url_prefix="/clients")

@clients.route("/")
@login_required
def dashboard():
    clients = Client.query.filter_by(user_id=current_user.id).all()
    return render_template("clients/dashboard.html", clients=clients)


@clients.route("/create", methods=["POST"])
@login_required
def create_client():
    name = request.form["name"]
    phone = request.form["phone"]

    client = Client(name=name, phone=phone, user_id=current_user.id)

    db.session.add(client)
    db.session.commit()

    return redirect(url_for("clients.dashboard"))
