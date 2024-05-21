from fastapi import FastAPI
from db import Database
from models.models import ProductModel
from routers.routers import router
from routers.users_routers import router_user

db = Database()
db.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.include_router(router)
app.include_router(router_user)