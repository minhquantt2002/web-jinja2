from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine(url_db)
engine = create_engine('mysql+pymysql://root:@localhost/blog')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    print('Connecting to database ...')
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
