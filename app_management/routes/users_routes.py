from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import UserSchema 

from app_management.services import users_services

user_router = APIRouter(prefix = "/users")
templates = Jinja2Templates(directory = "templates")

@user_router.get("/me")
def current_user_route(user: UserSchema = Depends(manager)):
    return user


@user_router.get('/new/user')
def ask_to_add_new_user(request: Request):
    return templates.TemplateResponse(
        "authentication/new_user.html",
        context={
            'request': request
        }
    )

@user_router.post('/new/user')
def create_new_user(firstname: Annotated[str, Form()]):
    user = {
        'firstname': firstname,
        'name': "nn",
        'id': 0,
        'email': "dd",
        'password': "kk",
        'role': "dnnd",
    }

    try:
        new_user = UserSchema.model_validate(user)
        print(new_user)
    except ValidationError:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bad credentials!"
        )
    users_services.add_new_user(new_user)
    return RedirectResponse(url='/account', status_code=302)
