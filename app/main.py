from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import route_user
import route_admin

app = FastAPI(
    docs_url='/swagger/api/docs',
    redoc_url='/api/redoc',
    title='MU'
)

templates = Jinja2Templates(directory="client/templates")
app.include_router(router=route_user.root_user)
app.include_router(router=route_admin.root_admin, prefix="/admin")


@ app.exception_handler(404)
def http_exception_handlers(request, exc):
    return templates.TemplateResponse(status_code=404, name="404.html", context={'request': request})


@ app.exception_handler(301)
def authorization(request, exc):
    return RedirectResponse('articles')
