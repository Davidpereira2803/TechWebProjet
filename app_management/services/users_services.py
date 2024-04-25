from sqlalchemy import select

from app_management.db_manager import Session

def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    for user in users_data:
        if user.email == email:
            return user
    return None