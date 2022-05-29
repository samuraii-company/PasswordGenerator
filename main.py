from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.router import router

app = FastAPI(title="PasswordGeneratorAPI", version="0.1.0")

app.include_router(router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to PasswordGenerator API"}


if __name__ == "__main__":
    uvicorn.run("main:app")
