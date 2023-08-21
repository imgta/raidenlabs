from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
