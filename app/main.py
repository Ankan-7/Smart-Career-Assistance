from fastapi import FastAPI
from app.database import engine, Base
from sqlalchemy import text
from app.models import User
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from app.routes.career import router as career_router
from app.models import UserActivity

app = FastAPI()
app.include_router(user_router)

app.include_router(auth_router)
app.include_router(career_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Career Navigator API Running "}


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return {"status": "Database connected "}
    except Exception as e:
        return {"error": str(e)}