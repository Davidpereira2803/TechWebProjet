from http.client import HTTPException
from requests import Session
from pydantic import ValidationError
from shema.menu import OrderSchema
from sqlalchemy import select
from sqlalchemy.orm import joinedload




def add_order(new_order: OrderSchema):
    with Session() as session:
        order = order(menu_id= new_order.menu_id,
                      order_date=new_order.order_date,
                      quantity=new_order.quantity,
                      customer_email=new_order.customer_email)
        session.add(order)
        session.commit()
    return order



def delete_menu_by_order(delete_name: str):
    with Session() as session:
        statement = select(order).filter_by(name=delete_name)
        order = session.scalars(statement).one_or_none()

        if order is not None:
            session.delete(order)
            session.commit()


def edit_order(order_to_edit: str, order: OrderSchema):
    with Session() as session:
        statement = select(order).filter_by(name=order_to_edit)
        existing_order = session.scalars(statement).one()

        existing_order.name = order.name
        existing_order.id = order.id
        existing_order.restaurant_id = order.restaurant_id
        existing_order.category = order.category
        existing_order.price = order.price
        existing_order.owner_email = order.owner_email
        existing_order.status = order.status

        session.commit()
