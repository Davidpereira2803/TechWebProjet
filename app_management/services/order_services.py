from sqlalchemy import select

from app_management.db_manager import Session
from app_management.sql.sql_models import Dish, Order
from app_management.schema.schema import DishSchema, OrderSchema

def add_to_basket(id):
    with Session() as session:
        statement = select(Dish).filter_by(dishid= id)
        dish = session.scalars(statement).one()
        
        order = Order(
            orderid= 1,
            clientid= 1,
            dishes= dish.dishname,
            orderprice= 10,
            complete= False, 
        )

        session.add(order)
        session.commit()
