# Standard imports
import json

# Third party imports
import flask

# Application imports
import db
import models


root = flask.Blueprint("users", __name__)
table = models.user.User


@root.route("/", methods=("GET",))
def view_all():
    query = db.session.query(table)

    return json.dumps([user.to_dict() for user in query.all()])


@root.route("/<user_id>", methods=("GET",))
def view_one(user_id):
    query = db.session.query(table)
    user = query.filter(table.id == user_id).first()

    return json.dumps(user.to_dict())


@root.route("", methods=("POST",))
def create():
    query = db.session.query(table)

    body = flask.request.get_json()
    username = body.get("username")
    password = body.get("password")
    locked = body.get("locked")

    user = query.filter(table.username == username).first()
    if user:
        return json.dumps({"id": user.id}), 300
    else:
        new_user = table(
            username=username, password=password, locked=locked
        )
        db.session.add(new_user)
        db.session.commit()

        return json.dumps({"id": new_user.id})


@root.route("/<user_id>", methods=("PUT",))
def edit(user_id):
    query = db.session.query(table)
    body = flask.request.get_json()
    user = query.filter(table.id == user_id).first()

    user.name = body.get("name", user.name)
    user.description = body.get("description", user.description)
    response = {
        "name": user.name,
        "description": user.description,
        "id": user.id,
    }

    db.session.commit()

    return json.dumps(response)


@root.route("/<user_id>", methods=("DELETE",))
def delete(user_id):
    query = db.session.query(table)
    user = query.filter(table.id == user_id).first()

    if user:
        db.session.delete(user)
        response = {"deleted": user.id}

        db.session.commit()

        return json.dumps(response)
    else:
        return json.dumps({"deleted": user_id}), 300
