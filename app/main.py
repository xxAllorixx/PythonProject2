from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import frontend

app = FastAPI()
"""app.include_router(books.router, tags=["books"])"""
app.include_router(frontend.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
