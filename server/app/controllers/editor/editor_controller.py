from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from schemas.editor.editor_schema import EditorCreate, EditorUpdate
from models.model import Editor
from fastapi import HTTPException

def get_all_editors():
    with Session(engine) as session:
        try:
            result = session.query(Editor).all()
            print("Query Result:", result)
            return result
        except SQLAlchemyError as exc:
            print(f"Database error:{exc}")
            raise HTTPException(status_code=500, detail= "Database error")


def get_editor_by_id(editor_id : int):
    with Session(engine) as session:
        try:
            result = session.query(Editor).filter(Editor.id == editor_id).first()
            if result is None:
                raise HTTPException(
                status_code=404, 
                detail=f"Editor with ID {editor_id} not found"
                )
            return result
        except SQLAlchemyError as exc:
            print(f"Database error: {exc}")
            raise HTTPException(
                status_code=500, 
                detail="Database error occurred"
            )
        

def create_editor(editor: EditorCreate):
    with Session(engine) as session:
        try:
            result = Editor(
                issue_id=editor.issue_id,

                firstname_en=editor.firstname_en,
                firstname_mn=editor.firstname_mn,
                firstname_tr=editor.firstname_tr,

                middlename_en=editor.middlename_en,
                middlename_mn=editor.middlename_mn,
                middlename_tr=editor.middlename_tr,

                lastname_en=editor.lastname_en,
                lastname_mn=editor.lastname_mn,
                lastname_tr=editor.lastname_tr,

                role_en=editor.role_en,
                role_mn=editor.role_mn,
                role_tr=editor.role_tr,

                suffix_en=editor.suffix_en,
                suffix_mn=editor.suffix_mn,
                suffix_tr=editor.suffix_tr
            )
            session.add(result)
            session.commit()
            session.refresh(result)
            return result
        
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500, 
                detail=f"Database error ocurred: {exc}"
        )
    
def update_editor(editor_id: int, editor: EditorUpdate):
    with Session(engine) as session:
        try:
            res = session.query(Editor).filter(Editor.id == editor_id).first()
            if res is None:
                raise HTTPException(
                status_code=404, 
                detail=f"Editor with ID {editor_id} not found"
                )

            update_data = editor.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(res, key, value)

            session.commit()
            session.refresh(res)
            return res
        
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500, 
                detail=f"Update execution error:{exc}"
            )