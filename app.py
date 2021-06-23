# Third party imports
import flask

# Application imports
import config
import routes


app = flask.Flask(config.config["app"]["name"], instance_relative_config=True)
app.config.from_mapping(config.config)
app.register_blueprint(routes.apis.items.root, url_prefix="/v1/items")
app.register_blueprint(
    routes.apis.permissions.root, url_prefix="/v1/permissions"
)
app.register_blueprint(routes.apis.tags.root, url_prefix="/v1/tags")
app.register_blueprint(routes.apis.users.root, url_prefix="/v1/users")
