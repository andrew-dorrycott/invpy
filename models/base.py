# Standard imports
import datetime
import urllib

# Third party imports
import sqlalchemy
import sqlalchemy.ext.declarative

# Application import
import config


BaseSQLAlchemy = sqlalchemy.ext.declarative.declarative_base()


def load_db():
    """
    Creates a SQLAlchemy session to be used by the controllers

    :param config: Configuration information provided by :meth:load_config
    :type config: dict
    :returns: SQLAlchemy Session
    :rtype: sqlalchemy.orm.session.Session
    """
    config.config["postgresql"]["password"] = urllib.parse.quote(
        config.config["postgresql"]["password"]
    )
    engine = sqlalchemy.create_engine(
        config.config["postgresql"]["sqlalchemy_uri"].format(
            **config.config["postgresql"]
        )
    )
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    return Session()


class Base:
    def __init__(self, **kwargs):
        """
        Initalizer

        :returns: Nothing
        :rtype: None
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        """
        Custom String representation

        :returns: String representation of the data
        :rtype: str
        """
        return "<{}(id='{id}', name='{name}')>".format(
            self.__class__.__name__, **self.__dict__
        )

    def to_dict(self):
        """
        Custom Dictionary/Json-able representation

        :returns: Dict representation of the data
        :rtype: dict
        """
        response = {}

        for key, value in self.__class__.__dict__.items():
            sqlattribute = sqlalchemy.orm.attributes.InstrumentedAttribute
            if isinstance(value, sqlattribute):
                value = getattr(self, key)
            else:
                continue  # Skip key

            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(value, (tuple, list)):
                value = [item.to_dict() for item in value]

            response[key] = value

        return response
