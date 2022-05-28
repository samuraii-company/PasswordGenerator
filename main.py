from fastapi import FastAPI
from api.router import router

app = FastAPI(title="PasswordGeneratorAPI", version="0.1.0")

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to PasswordGenerator API"}
