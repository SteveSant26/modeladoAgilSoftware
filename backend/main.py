import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import Base, engine
from apps.fruits import fruit_router
from apps.category import category_router


app = FastAPI(title="Fruits backend", description="This is an APIabout fruits")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(fruit_router)
app.include_router(category_router)

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
