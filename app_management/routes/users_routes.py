from fastapi import APIRouter, HTTPException, Request, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from app_management.user_login import manager
from app_management.schema.user import UserSchema 


user_router = APIRouter(prefix = "/users")
templates = Jinja2Templates(directory = "templates")

@user_router.get("/me")
def current_user_route(user: UserSchema = Depends(manager)):
    return user