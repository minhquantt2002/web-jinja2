from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import Session
from . import model
from .schemas import article_schema, video_schema


def read_articles_by_user(db: Session):
    stmt = select(model.Article)
    return db.execute(stmt).scalars().all()


def read_articles_by_admin(db: Session):
    stmt = select(model.Article)
    return db.execute(stmt).scalars().all()


def read_article_by_id(db: Session, id: int):
    stmt = select(model.Article).filter(model.Article.id == id)
    return db.execute(stmt).scalars().first()


def read_top_articles(db: Session):
    stmt = select(model.Article).order_by(model.Article.view.desc())
    return db.execute(stmt).scalars().all()


def increment_view(db: Session, id: int):
    stmt = select(model.Article.view).filter(model.Article.id == id)
    ss = db.execute(stmt).first()
    db.query(model.Article).filter(
        model.Article.id == id).update({'view': ss.view + 1})
    db.commit()


def create_article_by_admin(db: Session, article: article_schema.ArticleCreate) -> None:
    article = model.Article(**article.dict())
    db.add(article)
    db.flush()


def update_article_by_admin(db: Session, id: int, article: article_schema.ArticleUpdate) -> None:
    stmt = update(model.Article).where(model.Article.id == id).values(
        **article.dict()).execution_options(synchronize_session='fetch')
    db.execute(stmt)
    db.flush()


def delete_article_by_admin(db: Session, id: int) -> None:
    stmt = delete(model.Article).where(
        model.Article.id == id)
    db.execute(stmt)
    db.flush()


"""Video"""


def read_videos(db: Session):
    stmt = select(model.Video)
    return db.execute(stmt).scalars().all()


def read_video_by_id(db: Session, id: int):
    stmt = select(model.Video).filter(model.Video.id == id)
    return db.execute(stmt).scalars().first()


def create_video_by_admin(db: Session, video: video_schema.VideoCreate) -> None:
    video = model.Video(**video.dict())
    db.add(video)
    db.flush()


def update_video_by_admin(db: Session, id: int, video: video_schema.VideoCreate):
    stmt = update(model.Video).where(model.Video.id == id).values(
        **video.dict()).execution_options(synchronize_session='fetch')
    db.execute(stmt)
    db.flush()


def delete_video_by_admin(db: Session, id: int) -> None:
    stmt = delete(model.Video).where(
        model.Video.id == id)
    db.execute(stmt)
    db.flush()


def get_accound(db: Session, email: str, password: str):
    stmt = select(model.Account).filter(
        and_(model.Account.email == email, model.Account.hashed_password == password))
    return db.execute(stmt).scalars().first()
