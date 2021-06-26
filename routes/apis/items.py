# Standard imports
import json

# Third party imports
import flask

# Application imports
import db
import models


routes = flask.Blueprint("items", __name__, url_prefix="/v1/items")
table = models.item.Item


@routes.route("/", methods=("GET",))
def view_all():
    query = db.session.query(table)

    return json.dumps([items.to_dict() for items in query.all()])


@routes.route("/<item_id>", methods=("GET",))
def view_one(item_id):
    query = db.session.query(table)
    user = query.filter(table.id == item_id).first()

    return json.dumps(user.to_dict())


@routes.route("", methods=("POST",))
def create():
    query = db.session.query(table)

    body = flask.request.get_json()
    name = body.get("name")
    description = body.get("description")
    quantity = body.get("quantity")
    image = body.get("image")

    user = query.filter(table.name == name).first()
    if user:
        return json.dumps({"id": user.id}), 300
    else:
        new_permission = table(
            name=name, description=description, quantity=quantity, image=image
        )
        db.session.add(new_permission)
        db.session.commit()

        return json.dumps({"id": new_permission.id})


@routes.route("/<item_id>", methods=("PUT",))
def edit(item_id):
    query = db.session.query(table)
    body = flask.request.get_json()
    user = query.filter(table.id == item_id).first()

    user.name = body.get("name", user.name)
    user.description = body.get("description", user.description)
    response = {
        "name": user.name,
        "description": user.description,
        "id": user.id,
    }

    db.session.commit()

    return json.dumps(response)


@routes.route("/<item_id>", methods=("DELETE",))
def delete(item_id):
    query = db.session.query(table)
    user = query.filter(table.id == item_id).first()

    if user:
        db.session.delete(user)
        response = {"deleted": user.id}

        db.session.commit()

        return json.dumps(response)
    else:
        return json.dumps({"deleted": item_id}), 300
