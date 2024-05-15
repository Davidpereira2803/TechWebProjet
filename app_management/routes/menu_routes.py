from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import DishSchema 
from app_management.services import menu_services

menu_router = APIRouter(prefix = "/menu")
templates = Jinja2Templates(directory = "templates")

@menu_router.get('/all/dishes')
def get_menu_card(request: Request):
    menu = menu_services.get_menu()
    return templates.TemplateResponse(
        request,
        "menu.html",
        context={
            'menu': menu
        }
    )

@menu_router.get('/add/dish')
def ask_to_add_new_dish(request: Request):
    return templates.TemplateResponse(
        "new_dish.html",
        context={'request': request}
    )