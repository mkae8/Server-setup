from fastapi import APIRouter
from controllers.author.author_controller import (get_all_authors, get_author_by_id, creatre_author,update_author)
from schemas.author.author_schema import AuthorCreate, AuthorUpdate, AuthorResponse

authorRouter = APIRouter()

@authorRouter.get("/author")
def fetch_authors():
    return get_all_authors()

@authorRouter.get("/author/{author_id}", response_model=AuthorResponse)
def fetch_atricle_by_id(author_id:int):
    return get_author_by_id(author_id)

@authorRouter.post("/author", response_model=AuthorResponse , status_code=201)
def add_author(author:AuthorCreate):
    return creatre_author(author)


@authorRouter.put("/author/{author_id}", response_model=AuthorResponse)
def modify_author(author_id: int , author:AuthorUpdate):
    return update_author(author_id, author)