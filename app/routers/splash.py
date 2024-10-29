from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Initialize the router for the splash page
router = APIRouter()

# Specify the directory where the templates are located
templates = Jinja2Templates(directory="app/templates")

# Route for the splash/welcome page
@router.get("/")
def splash_page(request: Request):
    # Render the splash.html template with the request object
    return templates.TemplateResponse("splash.html", {"request": request})
