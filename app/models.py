import sqlalchemy as sa

from datetime import datetime

from app import db
from app import exceptions


class Simple(db.Model):
    __tablename__ = "simples"
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    number = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != "id"}

    @staticmethod
    def from_json(json):
        try:
            created_at = datetime.now()
            simple = Simple(
                **json,
                created_at=created_at,
                updated_at=created_at,
            )
            return simple
        except (KeyError, TypeError) as e:
            raise exceptions.ValidationError(e)

