from fastapi import FastAPI
from app.routes.users import user_router
app = FastAPI(
   title="Movex User System API",
   description="An API for the Movex movie platform system",
   version="1.0.0"
)
app.include_router(user_router) 

@app.get("/")
async def health_check():
   return {"status": "ok",
           "name": "Movex"}
