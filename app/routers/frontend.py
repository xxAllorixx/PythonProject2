from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data.books import book
from app.routers.books import add_book
from app.models.book import Book
from fastapi import Form

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    text = {
        "title": "Welcome to the library",
        "content": "Have you ever seen this place?"
    }
    return templates.TemplateResponse(request=request, name="home.html", context={"text": text})
@router.get("/book_list", response_class=HTMLResponse)
def show_book_list(request: Request):
    context = {
        "books": list(book.values())
    }
    return templates.TemplateResponse(request=request, name="list.html", context=context)
@router.get("/show_add_book", response_class=HTMLResponse)
def show_add_book_form(request: Request):
    return templates.TemplateResponse(request=request, name="add.html")
@router.post("/add_book", response_class=HTMLResponse)
def add_book_form(request: Request, id: int = Form(...), title: str = Form(...), author: str = Form(...), review: int = Form(...)):
    new_book = Book(id=id, title=title, author=author, review=review)
    try:
        result = add_book(new_book)  # <-- chiama la funzione del router books
        message = result["message"]
    except HTTPException as error:
        message = error.detail

    return templates.TemplateResponse(
        request=request,
        name="add.html",
        context={"request": request, "message": message}
    )



