from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_url import Base


def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_table()
    return app

def create_table():
    Base.metadata.create_all(bind=engine)

app=start_app()

@app.get('/')
def hello_api():
    return {"detail":"Hello there!"}
