# Third party imports
import sqlalchemy

# Application imports
from . import base
from . import permission


class User(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
    )
    username = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    locked = sqlalchemy.Column(sqlalchemy.Boolean)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)

    permissions = sqlalchemy.orm.relationship(
        permission.Permission, secondary="permissions_to_users"
    )

    def to_dict(self):
        """
        Custom Dictionary/Json-able representation

        :returns: Dict representation of the data
        :rtype: dict
        """
        return {
            "id": self.id,
            "username": self.username,
            "locked": self.locked,
            "creation_date": self.creation_date.strftime("%Y-%m-%s %H:%M:%S"),
            "modification_date": self.modification_date.strftime(
                "%Y-%m-%s %H:%M:%S"
            ),
        }
