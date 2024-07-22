from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .database import get_db
from . import crud

templates = Jinja2Templates(directory="app/client/templates")

root_user = APIRouter(tags=['APIs User'])


@root_user.get('/', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def user_read_articles(request: Request, db: Session = Depends(get_db)):
    articles = crud.read_articles_by_user(db=db)
    response_data = {'request': request, 'articles': articles}
    return templates.TemplateResponse('user/home.html', response_data)


@root_user.get('/articles/{id}', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def user_read_article(request: Request, id: int, db: Session = Depends(get_db)):
    article = crud.read_article_by_id(db=db, id=id)
    crud.increment_view(db=db, id=id)
    response_data = {'request': request, 'article': article}
    return templates.TemplateResponse('user/article.html', response_data)


@root_user.get('/videos', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def user_read_course(request: Request, db: Session = Depends(get_db)):
    videos = crud.read_videos(db=db)
    response_data = {'request': request, 'videos': videos}
    return templates.TemplateResponse('user/videos.html', response_data)


@root_user.get('/top-articles', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def user_read_top_articles(request: Request, db: Session = Depends(get_db)):
    articles = crud.read_top_articles(db=db)
    response_data = {'request': request, 'articles': articles}
    return templates.TemplateResponse('user/top_articles.html', response_data)
