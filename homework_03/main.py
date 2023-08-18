import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ROOT"}


@app.get("/ping/", status_code=200)
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)  #
