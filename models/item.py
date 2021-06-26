# Third party imports
import sqlalchemy

# Application imports
from . import base
from . import tag


class Item(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "items"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
    )
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    image = sqlalchemy.Column(sqlalchemy.String)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)

    tags = sqlalchemy.orm.relationship(tag.Tag, secondary="tags_to_items")
