from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="URL Shortner")
app.include_router(router)