from fastapi import APIRouter, HTTPException, Request, status
from fastapi.response import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

user_router = APIRouter(prefix = "/users")
templates = Jinja2Templates(directory = "templates")

@user_router.get("/me")
def current_user_route(user: UserSchema = Depends(manager)):
    return user