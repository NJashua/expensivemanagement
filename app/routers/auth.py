from fastapi import APIRouter, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud.user import create_user
from database.connection import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "message": None})

@router.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),  # Change here
    db: Session = Depends(get_db)
):
    message = None
    try:
        # Align the field name with the UserCreate schema
        user_data = UserCreate(
            username=username,
            email=email,
            password=password,
            confirmPassword=confirm_password  # Keep this as is or change to confirm_password if you choose that option
        )
        db_user = create_user(db, user_data)
        message = "User registered successfully! You can now log in."
    except Exception as e:
        message = "An error occurred during registration: " + str(e)

    return templates.TemplateResponse("register.html", {"request": request, "message": message})
