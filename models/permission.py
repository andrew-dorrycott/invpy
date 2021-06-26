# Third party imports
import sqlalchemy

# Application imports
from . import base


class Permission(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "permissions"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
    )
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)

    def to_dict(self):
        """
        Custom Dictionary/Json-able representation

        :returns: Dict representation of the data
        :rtype: dict
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            "modification_date": self.modification_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
