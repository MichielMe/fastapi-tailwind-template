from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.core import settings

router = APIRouter()
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        'pages/index.html',
        {
            'title': 'Home',
            'request': request,
        }
    )
    
@router.get('/styletest', response_class=HTMLResponse)
def styletest(request: Request):
    return templates.TemplateResponse(
        'pages/styletest.html',
        {
            'title': 'Style Test',
            'request': request,
        }
    )