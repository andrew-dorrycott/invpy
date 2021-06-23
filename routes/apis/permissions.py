# Standard imports
import json

# Third party imports
import flask

# Application imports
import db
import models


root = flask.Blueprint("permissions", __name__)
table = models.permission.Permission


@root.route("/", methods=("GET",))
def view_all():
    query = db.session.query(table)

    return json.dumps([permission.to_dict() for permission in query.all()])


@root.route("/<permission_id>", methods=("GET",))
def view_one(permission_id):
    query = db.session.query(table)
    user = query.filter(table.id == permission_id).first()

    return json.dumps(user.to_dict())


@root.route("", methods=("POST",))
def create():
    query = db.session.query(table)

    body = flask.request.get_json()
    name = body.get("name")
    description = body.get("description")

    user = query.filter(table.name == name).first()
    if user:
        return json.dumps({"id": user.id}), 300
    else:
        new_permission = table(name=name, description=description)
        db.session.add(new_permission)
        db.session.commit()

        return json.dumps({"id": new_permission.id})


@root.route("/<permission_id>", methods=("PUT",))
def edit(permission_id):
    query = db.session.query(table)
    body = flask.request.get_json()
    user = query.filter(table.id == permission_id).first()

    user.name = body.get("name", user.name)
    user.description = body.get("description", user.description)
    response = {
        "name": user.name,
        "description": user.description,
        "id": user.id,
    }

    db.session.commit()

    return json.dumps(response)


@root.route("/<permission_id>", methods=("DELETE",))
def delete(permission_id):
    query = db.session.query(table)
    user = query.filter(table.id == permission_id).first()

    if user:
        db.session.delete(user)
        response = {"deleted": user.id}

        db.session.commit()

        return json.dumps(response)
    else:
        return json.dumps({"deleted": permission_id}), 300
