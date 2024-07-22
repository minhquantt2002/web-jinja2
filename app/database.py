from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:minhquan223@localhost:5432/abcd')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    print('Connecting to database ...')
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
