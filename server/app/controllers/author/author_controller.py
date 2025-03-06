from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from fastapi import HTTPException

from models.model import Author
from schemas.author.author_schema import AuthorCreate, AuthorUpdate

def get_all_authors():
    with Session(engine) as session:
        try:
            result = session.query(Author).all()
            print("Query Result:", result)
            return result
        except SQLAlchemyError as exc:
            print(f"Database error:{exc}")
            raise HTTPException(status_code=500, detail="Database error")

def get_author_by_id(author_id:int):
    with Session(engine) as session:
        try:
            result = session.query(Author).filter(Author.id == author_id ).first()
            if result is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Author with ID {author_id} not found"
                )
            return result
        except SQLAlchemyError as exc:
            print(f"Database error:{exc}")
            raise HTTPException(
                status_code=500,
                detail="Database error occured"
            )
        
def creatre_author(author:AuthorCreate):
    with Session(engine) as session:
        try:
            result = Author(
                article_id = author.article_id,

                firstname_en= author.firstname_en,
                firstname_mn= author.firstname_mn,
                firstname_tr= author.firstname_tr,

                middlename_en = author.middlename_en,
                middlename_mn = author.middlename_mn,
                middlename_tr = author.middlename_tr,

                lastname_en =  author.lastname_en,
                lastname_mn =  author.lastname_mn,
                lastname_tr =  author.lastname_tr,

                suffix_en =  author.suffix_en,
                suffix_mn =  author.suffix_mn,
                suffix_tr =  author.suffix_tr,
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
def update_author(author_id : int, article:AuthorUpdate):
    with Session(engine) as session:
        try:
            result = session.query(Author).filter(Author.id == author_id).first()
            if result is None:
                raise HTTPException(
                    status_code=404, 
                    detail= f"Author with ID {author_id} not found"
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
