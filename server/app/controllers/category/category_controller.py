from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from schemas.category.category_schema import CategoryCreate, CategoryUpdate
from models.model import Category
from fastapi import HTTPException

def get_all_categories():
    with Session(engine) as session:
        try:
            result = session.query(Category).all()
            print("Query Result:", result)
            return result
        except SQLAlchemyError as exc:
            print(f"Dataabse error:{exc}")
            raise HTTPException(status_code=500, detail="Database error")
    
def create_category(category: CategoryCreate):
    with Session(engine) as session:
        try:
            result = Category(
                issue_id=category.issue_id,
                title_en = category.title_en,
                title_mn = category.title_mn,
                title_tr = category.title_tr,
            )
            session.add(result)
            session.commit()
            session.refresh(result)
            return result
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500, detail=f"Database error ocurred: {exc}"
            )

def update_category(category_id: int, category: CategoryUpdate):
    with Session(engine) as session:
        try:
            res = session.query(Category).filter(Category.id == category_id).first()
            if res:
                if category.title_en is not None:
                    res.title_en = category.title_en
                if category.title_mn is not None:
                    res.title_mn = category.title_mn
                if category.title_tr is not None:
                    res.title_tr = category.title_tr
                session.commit()
                session.refresh(res)
            return res
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Update execution error: {exc}"
            )



            
            
