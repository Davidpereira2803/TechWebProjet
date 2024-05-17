from sqlalchemy import select, or_

from app_management.db_manager import Session
from app_management.sql.sql_models import Table

def book_table(people_count, day, time, user):
    with Session() as session:
        statement = select(Table).where(
            Table.available == True,
            or_(
                Table.tablecapacity == people_count, 
                Table.tablecapacity > people_count
                )
        ).order_by(Table.tablecapacity).limit(1)
        table = session.scalars(statement).one()

        table.clientid = user.id
        table.available = False
        table.day = day
        table.time = time

        session.commit()

