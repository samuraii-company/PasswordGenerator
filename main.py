from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from fastapi import HTTPException, status

from fastapi.responses import JSONResponse

from core.generator import PasswordCredentials

from api import services


app = FastAPI(title="PasswordGeneratorAPI", version="0.1.0")

origins = ["*"]

MAX_SYMBOLS = 101
MIN_SYMBOLS = 20

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/v1/")
async def root():
    return {"message": "Welcome to PasswordGenerator API"}


@app.get("/api/v1/password")
def generate_password(
    count: int = 20,
    numbers: bool = False,
    symbols: bool = False,
):
    """Generate Password"""

    if count > MAX_SYMBOLS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum password length 100 symbols",
        )

    credentials = PasswordCredentials(
        count if count >= MIN_SYMBOLS else MIN_SYMBOLS, numbers, symbols
    )

    _password = services.create(credentials)

    return JSONResponse(content={"password": _password}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app")
