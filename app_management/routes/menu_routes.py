from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import DishSchema, UserSchema
from app_management.services import menu_services

menu_router = APIRouter(prefix = "/menu")
templates = Jinja2Templates(directory = "templates")

@menu_router.get('/all/dishes')
def get_menu_card(request: Request, user: UserSchema = Depends(manager.optional)):
    menu = menu_services.get_menu()
    return templates.TemplateResponse(
        request,
        "/dishes/menu.html",
        context={
            'menu': menu, 'active_user': user
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
    return RedirectResponse(url="/menu/all/dishes", status_code=302)

@menu_router.get('/remove/dish')
def ask_to_remove_dish(request: Request):
    return templates.TemplateResponse(
        "dishes/remove_dish.html",
        context={'request': request}
    )

@menu_router.post('/remove/dish')
def remove_dish(dishid: Annotated[str, Form()]):
    menu_services.remove_dish_by_id(dishid)
    return RedirectResponse(url="/menu/all/dishes", status_code=302)

@menu_router.get('/edit/dish')
def ask_to_edit_dish(request: Request):
    return templates.TemplateResponse(
        "dishes/edit_dishes.html",
        context={'request': request}
    )

@menu_router.post('/edit/dish')
def edit_dish(dishid: Annotated[str, Form()], dishname: Annotated[str, Form()], dishtype: Annotated[str, Form()], price: Annotated[str, Form()]):
    new_dish = {
        'dishid': dishid,
        'dishname': dishname,
        'dishtype': dishtype, 
        'price': price
    }
    try:
        dish = DishSchema.model_validate(new_dish)
    except ValidationError as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dish values have are not correct/ complete!",
        )

    menu_services.edit_dish_by_id(dishid, dish)
    return RedirectResponse(url="/menu/all/dishes", status_code=302)