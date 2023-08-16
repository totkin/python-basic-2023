from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello Index!"}


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello {name}!"}


@app.get("/items")
def items_list():
    return {
        "items": [
            {"id": 1, "name": "item-01"},
            {"id": 2, "name": "test"}
        ]
    }

@app.get("/items/{item_id}/")
def get_item(item_id:int):
    return {
        "data": {
            "id":item_id/2,"name":f"item-{item_id}"}
    }

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
