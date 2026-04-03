from fastapi import FastAPI
from app.routes import users
app = FastAPI(
   title="Movex User System API",
   description="An API for the Movex movie platform system",
   version="1.0.0"
)
app.include_router(users.router) 

@app.get("/")
async def health_check():
   return {"status": "ok",
           "name": "Movex"}
