from routes import router
from fastapi import FastAPI
import uvicorn


if __name__ == "__main__":

    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host="localhost", port=8000)
