from fastapi import APIRouter, Request, HTTPException, Query, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data.books import book
from app.models.book import Book
from app.routers.books import add_book, delete_book, delete_all_books, get_book_by_id

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

@router.post("/delete_a_book", response_class=HTMLResponse)
def del_a_book(request: Request, id: int = Form(...)):
    try:
        result = delete_book(id)  # <-- chiama la funzione del router books
        message = result["message"]
    except HTTPException as error:
        message = error.detail

    return templates.TemplateResponse(request=request, name="edit.html", context={"message": message})
@router.get("/search", response_class=HTMLResponse)
def show_search_form(request: Request):
    return templates.TemplateResponse(request=request, name="search.html")
@router.get("/find_a_book", response_class=HTMLResponse)
def get_book(request: Request, id: int = Query(...)):
    try:
        result = get_book_by_id(id)  # <-- chiama la funzione del router books
        message = f"Libro con {result} è stato trovato."
    except HTTPException as error:
        message = error.detail

    return templates.TemplateResponse(request=request, name="search.html", context={"message": message})







