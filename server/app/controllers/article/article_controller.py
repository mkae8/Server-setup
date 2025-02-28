from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from fastapi import HTTPException

from models.model import Article
from schemas.article.article_schema import ArticleCreate, ArticleUpdate

def get_all_articles():
    with Session(engine) as session:
        try:
            result = session.query(Article).all()
            print("Query Result:", result)
            return result
        except SQLAlchemyError as exc:
            print(f"Database error:{exc}")
            raise HTTPException(status_code=500, detail="Database error")

def get_article_by_id(artile_id:int):
    with Session(engine) as session:
        try:
            result = session.query(Article).filter(Article.id == artile_id ).first()
            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Article with ID {artile_id} not found"
                )
            return result
        except SQLAlchemyError as exc:
            print(f"Database error:{exc}")
            raise HTTPException(
                status_code=500,
                detail="Database error occured"
            )
        
def creatre_atricle(article:ArticleCreate):
    with Session(engine) as session:
        try:
            result = Article(
                category_id = article.category_id,
                file_url = article.file_url, 
                title_en = article.title_en,
                title_mn = article.title_mn,
                title_tr = article.title_tr, 
                placement_begin = article.placement_begin,
                placement_end = article.placement_end

            )
            session.add(result)
            session.commit()
            session.refresh(result)
            return result 
        
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {exc}"
            )
def update_article(article_id : int, article:ArticleUpdate):
    with Session(engine) as session:
        try:
            result = session.query(Article).filter(Article.id == article_id).first()
            if result is None:
                raise HTTPException(
                    status_code=404, 
                    detail= f"Article with ID {article_id} not found"
                )
            update_data = article.dict(exclude_unset=True)
            for key , value in update_data.items():
                setattr(result, key , value)
            session.commit()
            session.refresh(result)
            return result
            
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Update execution error:{exc}"
            )
