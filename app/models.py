import sqlalchemy as sa

from app import db


class Simple(db.Model):
    __tablename__ = "simples"
    
    id = sa.Column(sa.Integer, primary_key=True)
    string = sa.Column(sa.String)
