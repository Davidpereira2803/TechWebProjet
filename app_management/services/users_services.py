import random
from sqlalchemy import select

from app_management.db_manager import Session
from app_management.sql.sql_models import User
from app_management.schema.schema import UserSchema

def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    for user in users_data:
        if user.email == email:
            return user
    return None

def add_new_user(user_values: UserSchema):
    with Session() as session:
        user = User(
            firstname = user_values.firstname,
            name = user_values.name,
            id = generate_id(),
            email = user_values.email,
            password = user_values.password,
            role = "client",
        )
        session.add(user)
        session.commit()
    
    return user

def generate_id():
    result = 1
    for i in range(10):
        result = result + random.randint(1,10) * result

    return result
    

