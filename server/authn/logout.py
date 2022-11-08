from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="client/templates")


@router.post("/logout", response_class=HTMLResponse, status_code=status.HTTP_304_NOT_MODIFIED)
def login(request: Request):
    response = RedirectResponse("login")
    response.delete_cookie(key="access_token")
    return response
