from fastapi import FastAPI
from routes import router
from logger import log_event
import uvicorn

log_event("INFO", "Start System API")

app = FastAPI()


try:
    app.include_router(router)
    log_event("INFO", "All routers connected")
except Exception as e:
    log_event("ERROR", f"Failed to connected routers {str(e)}")

if __name__ == "__main__":
    log_event("INFO", "connected to server")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)