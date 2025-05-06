from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form
from app.data.books import book
from app.models.book import Book
from app.routers.books import add_book
from app.routers.books import delete_all_books

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

@router.get("/edit_list", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(request=request, name="edit.html")

@router.post("/add_book", response_class=HTMLResponse)
def add_book_form(request: Request, id: int = Form(...), title: str = Form(...), author: str = Form(...), review: int = Form(...)):
    new_book = Book(id=id, title=title, author=author, review=review)
    try:
        result = add_book(new_book)  # <-- chiama la funzione del router books
        message = result["message"]
    except HTTPException as error:
        message = error.detail

    return templates.TemplateResponse(request=request, name="edit.html",context = {"message": message})

@router.post("/delete_all_books", response_class=HTMLResponse)
def del_all_books(request: Request):
    message = delete_all_books()
    return templates.TemplateResponse(request=request, name="edit.html",context = {"message": message})



