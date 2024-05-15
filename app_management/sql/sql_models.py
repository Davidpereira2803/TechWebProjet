from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app_management.db_manager import Base

class User(Base):
    __tablename__ = 'users'

    firstname: Mapped[str] = mapped_column(String(72))
    name: Mapped[str] = mapped_column(String(72))
    id: Mapped[int] = mapped_column(Integer(), primary_key= True, unique= True)
    email: Mapped[str] = mapped_column(String(72))
    password: Mapped[str] = mapped_column(String(72))
    role: Mapped[str] = mapped_column(String(72))

class Dish(Base):
    __tablename__ = 'dishes'

    dishid: Mapped[int] = mapped_column(Integer(), primary_key= True, unique= True)
    dishname: Mapped[str] = mapped_column(String(72))
    dishtype: Mapped[str] = mapped_column(String(72))
    price: Mapped[int] = mapped_column(Integer())