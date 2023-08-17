from fastapi import FastAPI
import uvicorn

from items_views import router as items_router

app = FastAPI()
app.include_router(items_router, prefix="/items")


@app.get("/")
async def index():
    return {"message": "Hello Index!"}


@app.get("/hello/")
async def hello(name: str = "World"):
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
