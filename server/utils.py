from fastapi import Request, HTTPException


def get_cookie(request: Request = None):
    if request.cookies.get('access_token') is None:
        raise HTTPException(status_code=401)


def has_cookie(request: Request = None):
    cookie = request.cookies.get('access_token')
    if cookie is not None:
        raise HTTPException(status_code=301)
