import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Books(SqlAlchemyBase):
    __tablename__ = "books"
    
    book_id = sqlalchemy.Column(sqlalchemy.Integer,
                                primary_key=True)
    book_name = sqlalchemy.Column(sqlalchemy.String)