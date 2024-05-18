from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app_management.db_manager import Base

class User(Base):
    __tablename__ = 'users'

    firstname: Mapped[str] = mapped_column(String(72))
    name: Mapped[str] = mapped_column(String(72))
    id: Mapped[int] = mapped_column(Integer, primary_key= True, unique= True)
    email: Mapped[str] = mapped_column(String(72), unique=True)
    password: Mapped[str] = mapped_column(String(72))
    role: Mapped[str] = mapped_column(String(72))

class Dish(Base):
    __tablename__ = 'dishes'

    dishid: Mapped[int] = mapped_column(Integer(), primary_key= True, unique= True)
    dishname: Mapped[str] = mapped_column(String(72))
    dishtype: Mapped[str] = mapped_column(String(72))
    price: Mapped[int] = mapped_column(Integer)

class Order(Base):
    __tablename__ = 'orders'

    orderid: Mapped[int] = mapped_column(Integer, primary_key= True, unique= True)
    clientid: Mapped[int] = mapped_column(Integer)
    dishes: Mapped[str] = mapped_column(String(72))
    orderprice: Mapped[int] = mapped_column(Integer)
    complete: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String(72))

class Table(Base):
    __tablename__ = 'tables'

    tableid: Mapped[int] = mapped_column(Integer, primary_key= True, unique= True)
    clientid: Mapped[int] = mapped_column(Integer)
    tablecapacity: Mapped[int] = mapped_column(Integer)
    day: Mapped[str] = mapped_column(String(72))
    time: Mapped[str] = mapped_column(String(72))
    available: Mapped[bool] = mapped_column(Boolean)

class Feedback(Base):
    __tablename__ = 'feedback'

    feedbackid: Mapped[int] = mapped_column(Integer, primary_key= True, unique= True)
    clientemail: Mapped[str] = mapped_column(String(72))
    feedback: Mapped[str] = mapped_column(String(72))