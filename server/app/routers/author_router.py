from fastapi import APIRouter
from controllers.author.author_controller import (get_all_authors, get_author_by_id, creatre_author,update_author)
from schemas.article.article_schema import ArticleCreate, ArticleResponse, ArticleUpdate

articleRouter = APIRouter()

@articleRouter.get("/article")
def fetch_articles():
    return get_all_authors()

@articleRouter.get("/article/{article_id}", response_model=ArticleResponse)
def fetch_atricle_by_id(article_id:int):
    return get_author_by_id(article_id)

@articleRouter.post("/article", response_model=ArticleResponse , status_code=201)
def add_article(article:ArticleCreate):
    return creatre_author(article)


@articleRouter.put("/article/{article_id}", response_model=ArticleResponse)
def modify_article(article_id: int , article:ArticleUpdate):
    return update_author(article_id, article)