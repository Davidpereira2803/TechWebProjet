from fastapi import FasatAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app_management.user_routes import user_router
from app_management.db_manager import create_database

templates = Jinja2Templates(directory = "templates")

app = FasatAPI(title = "Le coin de Namur")
app.mount("/static", StaticFiles(directory = "static"))
app.include_router(user_router)

@app.on_event('startup')
def on_startup():
    print("Server has started!")
    create_database()

@app.on_event('shutdown')
def on_shutdown():
    print("Server is down!")