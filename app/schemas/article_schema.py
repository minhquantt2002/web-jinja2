from datetime import datetime
from pydantic import BaseModel
from fastapi import Request


class ArticleBase(BaseModel):
    title: str
    description: str
    content: str
    image_url: str


class ArticleCreate(ArticleBase):
    view: int
    pass


class ArticleUpdate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    created: datetime

    class Config:
        orm_mode = True


class FormAticle:
    def __init__(self, request: Request):
        self.request: Request = request
        self.title: str = ""
        self.description: str = ""
        self.content: str = ""
        self.image_url: str = ""
        self.view: int = 0

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get('title')
        self.description = form.get('description')
        self.content = form.get('content')
        self.image_url = form.get('image_url')
