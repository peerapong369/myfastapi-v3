from fastapi import FastAPI

from models.database import engine, Base
from models.inventory import inventory_model
from models.users import users_model


from routers.inventory import inventory_rounter
from routers.users import user_router
from routers.auth import authen_router


app = FastAPI()
app.include_router(authen_router.router)
app.include_router(inventory_rounter.router)
app.include_router(user_router.router)



@app.get("/")
def hello():
    return {"hellow": "Fast-API"}


Base.metadata.create_all(engine)
inventory_model.Base.metadata.create_all(engine)
users_model.Base.metadata.create_all(engine)
