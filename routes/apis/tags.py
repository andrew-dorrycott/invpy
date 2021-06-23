# Standard imports
import json

# Third party imports
import flask

# Application imports
import db
import models


root = flask.Blueprint("tags", __name__)
table = models.tag.Tag


@root.route("/", methods=("GET",))
def view_all():
    query = db.session.query(table)

    return json.dumps([tag.to_dict() for tag in query.all()])


@root.route("/<tag_id>", methods=("GET",))
def view_one(tag_id):
    query = db.session.query(table)
    tag = query.filter(table.id == tag_id).first()

    return json.dumps(tag.to_dict())


@root.route("", methods=("POST",))
def create():
    query = db.session.query(table)

    body = flask.request.get_json()
    name = body.get("name")
    description = body.get("description")

    tag = query.filter(table.name == name).first()
    if tag:
        return json.dumps({"id": tag.id}), 300
    else:
        new_tag = table(name=name, description=description)
        db.session.add(new_tag)
        db.session.commit()

        return json.dumps({"id": new_tag.id})


@root.route("/<tag_id>", methods=("PUT",))
def edit(tag_id):
    query = db.session.query(table)
    body = flask.request.get_json()
    tag = query.filter(table.id == tag_id).first()

    tag.name = body.get("name", tag.name)
    tag.description = body.get("description", tag.description)
    response = {
        "name": tag.name, "description": tag.description, "id": tag.id
    }

    db.session.commit()

    return json.dumps(response)


@root.route("/<tag_id>", methods=("DELETE",))
def delete(tag_id):
    query = db.session.query(table)
    tag = query.filter(table.id == tag_id).first()

    db.session.delete(tag)
    response = {"deleted": tag.id}

    db.session.commit()

    return json.dumps(response)
