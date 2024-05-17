from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import OrderSchema
from app_management.services import order_services, menu_services

order_router = APIRouter(prefix="/orders")
templates = Jinja2Templates(directory="templates")

@order_router.get('/order')
def ask_to_order(request: Request):
    menu = menu_services.get_menu()
    return templates.TemplateResponse(
        "/dishes/order_page.html",
        context={'request': request, 'menu': menu}
    )

@order_router.post('/add/basket')
def add_dish_to_basket(dishid: Annotated[str, Form()]):
    order_services.add_to_basket(dishid)
    return RedirectResponse(url="/orders/order", status_code=302)
