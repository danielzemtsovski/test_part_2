from fastapi import FastAPI
from routes import router
from logger import log_event
import uvicorn

log_event("INFO", "Starting Employee Management System API")

app = FastAPI(title="Employee Management System")


try:
    app.include_router(router)
    log_event("INFO", "All routers included successfully")
except Exception as e:
    log_event("ERROR", f"Failed to include routers: {str(e)}")

if __name__ == "__main__":
    log_event("INFO", "Launching server on http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)