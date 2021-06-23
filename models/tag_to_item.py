# Third party imports
import sqlalchemy

# Application imports
from . import base


class TagToItem(base.Base, base.BaseSQLAlchemy):
    __tablename__ = "tags_to_items"

    item_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("items.id"),
        primary_key=True,
        nullable=False
    )
    tag_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("tags.id"),
        primary_key=True,
        nullable=False
    )
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime)
    modification_date = sqlalchemy.Column(sqlalchemy.DateTime)
