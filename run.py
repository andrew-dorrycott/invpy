# Standard imports
import logging

# Application imports
import app
import config
from routes import apis  # noqa: F401; force routes to load
import db  # noqa: F401; force db connection


LOGGER = logging.getLogger(__name__)

if __name__ == "__main__":
    LOGGER.info("Application starting")
    app.app.run(
        host=config.config["app"]["host"],
        port=config.config["app"]["port"],
        debug=config.config["app"]["debug"],
    )
