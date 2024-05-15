from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app_management.routes.users_routes import user_router
from app_management.db_manager import create_database

templates = Jinja2Templates(directory = "templates")

app = FastAPI(title = "Le coin de Namur")
app.mount("/static", StaticFiles(directory = "static"))
app.include_router(user_router)

@app.on_event('startup')
def on_startup():
    print("'Le coin de Namur' is on AIR!")
    create_database()

@app.on_event('shutdown')
def on_shutdown():
    print("'Le coin de Namur' is down!")