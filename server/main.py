from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from server.routes import route_admin, route_user
from server.authn import login, logout
from server import utils

app = FastAPI(
    docs_url='/swagger/api/docs',
    redoc_url='/api/redoc',
    title='Blog của anh em MU'
)

templates = Jinja2Templates(directory="client/templates")
app.include_router(router=route_user.root_user)
app.include_router(router=route_admin.root_admin, prefix='/admin', dependencies=[Depends(utils.get_cookie)])
app.include_router(router=login.router, prefix='/admin', dependencies=[Depends(utils.has_cookie)])
app.include_router(router=logout.router, prefix='/admin')

app.mount("/js", StaticFiles(directory="client/js"), name="static")


@app.exception_handler(404)
def http_exception_handlers(request, exc):
    return templates.TemplateResponse(status_code=404, name="404.html", context={'request': request})


@app.exception_handler(401)
def authorization(request, exc):
    return RedirectResponse('login')


@app.exception_handler(301)
def authorization(request, exc):
    return RedirectResponse('articles')
