
from sqlalchemy import *
from sqlalchemy.orm import session, sessionmaker, declarative_base

Base = declarative_base()
metadata = MetaData()


post = Table(
    'post', metadata,
    Column('id', Integer,primary_key=True),
    Column('tittle', VARCHAR,nullable=True),
    Column('body', Text,)
)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    tittle = Column(String)
    body = Column(String)

    def __repr__(self):
        return "<Post( tittle='%s', body='%s')>" % (
                         self.tittle, self.body)





def create_session():
    engine = create_engine('sqlite:///blogapp.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()


    
if __name__ == '__main__':
    session=create_session()
    
    post = Post()
    post.tittle='asdad'
    post.body='gggggg'
    
    
    #note = Post( tittle='first_tittle', body='a looooooooong post')
    #session.add(note)
    ##our_note = session.query(Post).filter_by(tittle='first_tittle').first()
    #print(session.add(note))
    session.add(post)
    session.commit()

    session.close()
    