from fastapi import APIRouter, HTTPException, Request, status, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from typing import Annotated

from app_management.user_login import manager
from app_management.schema.schema import TableSchema, UserSchema
from app_management.services import table_booking_services

table_router = APIRouter(prefix="/table")
templates = Jinja2Templates(directory="templates")

@table_router.get('/book/table')
def ask_to_book_a_table(request: Request):
    return templates.TemplateResponse(
        "dishes/book_table.html",
        context={'request': request}
    )

@table_router.post('/book/table')
def book_table(day: Annotated[str, Form()], time: Annotated[str, Form()], people_count: Annotated[str, Form()], user: UserSchema = Depends(manager.optional)):
    table_booking_services.book_table(people_count, day, time, user)
    return RedirectResponse(url="/users/home", status_code=302)