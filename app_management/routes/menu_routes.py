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
        "/dishes/menu.html",
        context={
            'menu': menu
        }
    )

@menu_router.get('/add/dish')
def ask_to_add_new_dish(request: Request):
    return templates.TemplateResponse(
        "dishes/new_dish.html",
        context={'request': request}
    )

@menu_router.post('/add/dish')
def add_new_dish(dishname: Annotated[str, Form()], dishtype: Annotated[str, Form()], price: Annotated[str, Form()]):
    dish = {
        'dishid': 0,
        'dishname': dishname,
        'dishtype': dishtype,
        'price': price
    }
    try:
        new_dish = DishSchema.model_validate(dish)
    except ValidationError as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dish details are not correct or complete!"
        )
    menu_services.add_dish(new_dish)
    return RedirectResponse(url="/users/home", status_code=302)

@menu_router.get('/book/table')
def ask_to_book_a_table(request: Request):
    return templates.TemplateResponse(
        "dishes/book_table.html",
        context={'request': request}
    )