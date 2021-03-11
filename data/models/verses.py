import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Verses(SqlAlchemyBase):
    __tablename__ = "verses"
    
    book_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("books.id"))
    chapter_id = sqlalchemy.Column(sqlalchemy.Integer)
    
    verse_id = sqlalchemy.Column(sqlalchemy.Integer)
    verse_content = sqlalchemy.Column(sqlalchemy.String)