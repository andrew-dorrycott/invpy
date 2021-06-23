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
            "quantity": self.quantity,
            "image": self.image,
            "creation_date": self.creation_date.strftime("%Y-%m-%s %H:%M:%S"),
            "modification_date": self.modification_date.strftime(
                "%Y-%m-%s %H:%M:%S"
            ),
        }
