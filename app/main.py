from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database.connection import engine, Base
from app.routers import auth, splash

# Initialize the FastAPI app
app = FastAPI()

# Create all database models and tables
Base.metadata.create_all(bind=engine)

# Serve static files (CSS, JavaScript, images, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize Jinja2 Templates
templates = Jinja2Templates(directory="app/templates")

# Include the routes from different routers
app.include_router(auth.router)
app.include_router(splash.router)
# app.include_router(auth.)