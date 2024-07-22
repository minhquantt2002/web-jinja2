from pydantic import BaseModel
from fastapi import Request


class VideoBase(BaseModel):
    title: str
    video_id: str


class VideoCreate(VideoBase):
    pass


class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True


class FormVideo:
    def __init__(self, request: Request):
        self.request: Request = request
        self.title: str = ""
        self.video_id: str = ""

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get('title')
        self.video_id = form.get('video_id')
