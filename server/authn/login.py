from fastapi import APIRouter, Request, Depends, status, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from server.authn.utils import LoginForm
from server.database import get_db
from server import crud

router = APIRouter()
templates = Jinja2Templates(directory="client/templates")


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@router.post("/login", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def login(request: Request, response: Response, db: Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    authn_token(response, form, db)
    return '/admin/articles'


def authn_token(response: Response, user: LoginForm, db: Session = Depends(get_db)):
    print(user.username, user.password)
    user = crud.get_accound(db=db, email=user.username, password=user.password)
    if not user:
        return RedirectResponse('login')

    response.set_cookie(
        key="access_token", max_age=30 * 30, value=f"Accound: '{user.email}' and '{user.hashed_password}'", httponly=True
    )
