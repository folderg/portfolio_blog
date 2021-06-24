from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    tittle = Column(String)
    body = Column(String)

    def __repr__(self):
        return "<User(name='%d', fullname='%s', nickname='%s')>" % (
                           self.id, self.tittle, self.body)