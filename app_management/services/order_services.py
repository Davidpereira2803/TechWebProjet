from sqlalchemy import select

from app_management.db_manager import Session
from app_management.sql.sql_models import Dish, Order
from app_management.schema.schema import DishSchema, OrderSchema

def get_orders():
    with Session() as session:
        statement = select(Order)
        orders = session.scalars(statement).all()

    return orders

def add_to_basket(id, user):
    with Session() as session:
        statement = select(Dish).filter_by(dishid= id)
        dish = session.scalars(statement).one()

        statement = select(Order)
        orders = session.scalars(statement).all()
        
        statement = select(Order).filter_by(clientid=user.id)
        try:
            current_order = session.scalars(statement).one()

            current_order.dishes = current_order.dishes + "," + dish.dishname
            current_order.orderprice = current_order.orderprice + dish.price
        except:
            order = Order(
                orderid= len(orders) + 1,
                clientid= user.id,
                dishes= dish.dishname,
                orderprice= dish.price,
                complete= False, 
            )

            session.add(order)

        session.commit()

def cancel_order(user):
    with Session() as session:
        statement = select(Order).filter_by(clientid=user.id)
        order = session.scalars(statement).one()

        session.delete(order)
        session.commit()

def remove_from_basket(dish_id, user):
    with Session() as session:
        statement = select(Order).filter_by(clientid=user.id)
        order = session.scalars(statement).one()

        statement = select(Dish).filter_by(dishid=dish_id)
        dish_to_remove = session.scalars(statement).one()

        order.dishes = order.dishes.replace(dish_to_remove.dishname, "", 1)
        order.orderprice = order.orderprice - dish_to_remove.price
        session.commit()

def mark_as_complete(order_id):
    with Session() as session:
        statement = select(Order).filter_by(orderid= order_id)
        order = session.scalars(statement).one()

        order.complete = True
        session.commit()