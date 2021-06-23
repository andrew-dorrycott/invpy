# Standard imports
import logging
import logging.config

# Third party imports
import yaml


LOGGER = logging.getLogger(__name__)


def load_config():
    """
    Loads the config.yaml

    :returns: Dict of loaded config.yaml
    :rtype: dict
    """
    with open("config.yaml", "r") as _file:
        return yaml.load(_file, Loader=yaml.FullLoader)


config = load_config()
logging.config.dictConfig(config["logging"])
LOGGER.debug("Config loaded")
