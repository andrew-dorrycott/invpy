# Third party imports
import sqlalchemy

# Application imports
from . import base


class PermissionToUser(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "permissions_to_users"

    permission_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("permissions.id"),
        primary_key=True,
        nullable=False
    )
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
        primary_key=True,
        nullable=False
    )
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)
