import sqlalchemy as sa

from app import db
from app import exceptions


class Simple(db.Model):
    __tablename__ = "simples"
    
    id = sa.Column(sa.Integer, primary_key=True)
    string = sa.Column(sa.String)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != "id"}

    @staticmethod
    def from_json(json):
        try:
            simple = Simple(
                string=json["string"]
            )
            return simple
        except KeyError as e:
            raise exceptions.ValidationError(e)

