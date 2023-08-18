import uvicorn
from fastapi import FastAPI
from view import router as router_ping

app = FastAPI()
app.include_router(router_ping, prefix="/ping")

@app.get("/")
def root():
    return {"message": "ROOT"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host='0.0.0.0', port=8000)  #
