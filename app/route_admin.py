from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import get_db
from schemas import article_schema, video_schema
import crud

templates = Jinja2Templates(directory="client/templates")

root_admin = APIRouter(tags=['APIs Admin'])

"""Article"""


@root_admin.get('/articles', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def show_articles(request: Request, db: Session = Depends(get_db)):
    articles = crud.read_articles_by_admin(db=db)
    response_data = {'request': request, 'articles': articles}
    return templates.TemplateResponse('admin/articles.html', response_data)


@root_admin.post('/articles/create', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def create_article(
        request: Request,
        db: Session = Depends(get_db)
):
    form_article = article_schema.FormAticle(request)
    await form_article.load_data()
    article = article_schema.ArticleCreate(**form_article.__dict__)
    crud.create_article_by_admin(db=db, article=article)
    db.commit()
    return '/admin/articles'


@root_admin.post('/articles/edit/id={id}', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def edit_article(
        request: Request,
        id: int,
        db: Session = Depends(get_db)
):
    form_article = article_schema.FormAticle(request)
    await form_article.load_data()
    article = article_schema.ArticleUpdate(**form_article.__dict__)
    crud.update_article_by_admin(db=db, id=id, article=article)
    db.commit()
    return '/admin/articles'


@root_admin.post('/articles/delete/id={id}', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
def delete_article(
        request: Request,
        id: int,
        db: Session = Depends(get_db)
):
    crud.delete_article_by_admin(db=db, id=id)
    db.commit()
    return '/admin/articles'


"""VIDEO"""


@root_admin.get('/videos', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def show_videos(request: Request, db: Session = Depends(get_db)):
    videos = crud.read_videos(db=db)
    response_data = {'request': request, 'videos': videos}
    return templates.TemplateResponse('admin/videos.html', response_data)


@root_admin.post('/videos/create', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def create_video(
        request: Request,
        db: Session = Depends(get_db)
):
    form_video = video_schema.FormVideo(request)
    await form_video.load_data()
    print(form_video.__dict__)
    video = video_schema.VideoCreate(**form_video.__dict__)
    crud.create_video_by_admin(db=db, video=video)
    db.commit()
    return '/admin/videos'


@root_admin.post('/videos/edit/id={id}', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def edit_video(
        request: Request,
        id: int,
        db: Session = Depends(get_db)
):
    form_video = video_schema.FormVideo(request)
    await form_video.load_data()
    video = video_schema.VideoCreate(**form_video.__dict__)
    crud.update_video_by_admin(db=db, id=id, video=video)
    db.commit()
    return '/admin/videos'


@root_admin.post('/videos/delete/id={id}', response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
def delete_video(
        request: Request,
        id: int,
        db: Session = Depends(get_db)
):
    crud.delete_video_by_admin(db=db, id=id)
    db.commit()
    return '/admin/videos'
