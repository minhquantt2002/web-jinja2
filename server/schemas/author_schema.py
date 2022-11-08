from pydantic import BaseModel


class AccoundBase(BaseModel):
    email: str


class AccoundCreate(AccoundBase):
    password: str


class Accound(AccoundBase):
    id: int

    class Config:
        orm_mode = True
