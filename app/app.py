import os

from fastapi import FastAPI
from mangum import Mangum

from app.user_routes import router as user_router

stage = os.environ.get("STAGE", None)
openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title="sam-fastapi-mangum-poc", debug=True, openapi_prefix=openapi_prefix)


@app.get("/ping", status_code=200, response_model=str, tags=["Ping Pong"])
def ping() -> str:
    return "pong"


app.include_router(user_router)

handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", port=8080, log_level="info", reload=True)
