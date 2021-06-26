# Third party imports
import sqlalchemy

# Application imports
from . import base


class Tag(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "tags"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
    )
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)
