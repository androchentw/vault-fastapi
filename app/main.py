from fastapi import FastAPI, Depends
from app.database import database, SessionLocal
from app.auth import oauth2_scheme, get_current_user
from app.models import example_table

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to test the connection
@app.get("/")
async def read_root(db: database = Depends(get_db)):
    return {"message": "Hello, FastAPI with PostgreSQL and HashiCorp Vault!"}

# Route to get a token
@app.post("/token")
async def login(form_data: OAuth2PasswordBearer = Depends(oauth2_scheme)):
    return {"access_token": form_data, "token_type": "bearer"}

# Protected route that requires a valid token
@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": "Hello, secured route!", "current_user": current_user}
