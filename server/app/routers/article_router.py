from fastapi import APIRouter
from controllers.article.article_controller import (get_all_articles, get_article_by_id, creatre_atricle,update_article)
from schemas.article.article_schema import ArticleCreate, ArticleResponse, ArticleUpdate

articleRouter = APIRouter()

@articleRouter.get("/article")
def fetch_articles():
    return get_all_articles()

@articleRouter.get("/article/{article_id}", response_model=ArticleResponse)
def fetch_atricle_by_id(article_id:int):
    return get_article_by_id(article_id)

@articleRouter.post("/article", response_model=ArticleResponse , status_code=201)
def add_article(article:ArticleCreate):
    return creatre_atricle(article)


@articleRouter.put("/article/{article_id}", response_model=ArticleResponse)
def modify_article(article_id: int , article:ArticleUpdate):
    return update_article(article_id, article)