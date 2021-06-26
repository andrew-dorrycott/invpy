# Third party imports
import flask

# Application imports
import config
import routes


app = flask.Flask(config.config["app"]["name"], instance_relative_config=True)
app.config.from_mapping(config.config)
app.register_blueprint(routes.apis.items.routes)
app.register_blueprint(routes.apis.permissions.routes)
app.register_blueprint(routes.apis.tags.routes)
app.register_blueprint(routes.apis.users.routes)
