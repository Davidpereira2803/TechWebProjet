from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import OrderSchema
from app_management.services import order_services

order_router = APIRouter(prefix="/orders")
templates = Jinja2Templates(directory="templates")

@order_router.get('/order')
def ask_to_order(request: Request):
    return templates.TemplateResponse(
        "/dishes/order_page.html",
        context={'request': request}
    )