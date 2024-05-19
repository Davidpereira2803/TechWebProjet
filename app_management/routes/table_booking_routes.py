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
        "tables/book_table.html",
        context={'request': request}
    )

@table_router.post('/book/table')
def book_table(day: Annotated[str, Form()], time: Annotated[str, Form()], people_count: Annotated[str, Form()], user: UserSchema = Depends(manager.optional)):
    table_booking_services.book_table(people_count, day, time, user)
    return RedirectResponse(url="/users/home", status_code=302)

@table_router.get('/manage')
def ask_to_manage_tables(request: Request):
    tables = table_booking_services.get_tables()
    return templates.TemplateResponse(
        "tables/tables.html",
        context={'request': request, 'tables': tables}
    )

@table_router.post('/change/availability')
def change_availability(tableid: Annotated[str, Form()]):
    table_booking_services.change_availability(tableid)
    return RedirectResponse(url="/table/manage", status_code=302)