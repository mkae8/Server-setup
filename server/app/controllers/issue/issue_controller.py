from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from schemas.issue.issue_schema import  IssueCreate, IssueUpdate
from models.model import Issue
from fastapi import HTTPException

def get_all_issues():
     with Session(engine) as session:
          try:
               result = session.query(Issue).all()
               print("Query Result:", result)
               return result
               
          except SQLAlchemyError as exc:
               print(f"Database error: {exc}")
               raise HTTPException(status_code=500, detail="Database error")

          
def get_issue_by_id(issue_id: int):
    with Session(engine) as session:
        try:
            result = session.query(Issue).filter(Issue.id == issue_id).first()
            if result is None:
                raise HTTPException(
                status_code=404,
                detail=f"Issue with ID {issue_id} not found"
            )
            return result
        except SQLAlchemyError as exc:
            print(f"Database error: {exc}")
            return{"Error_message": "Get execution error"}  

def create_issue(issue: IssueCreate):
    with Session(engine) as session:
        try:
            result = Issue(
                volume_id=issue.volume_id,
                image_url=issue.image_url,
                title_en=issue.title_en,
                title_mn=issue.title_mn,
                title_tr=issue.title_tr,
                description_en=issue.description_en,
                description_mn=issue.description_mn,
                description_tr=issue.description_tr
            )
            session.add(result)
            session.commit()
            session.refresh(result)
            return result
           
                
        except SQLAlchemyError as exc:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Database error occurred: {str(exc)}"
            )
def update_issue(issue_id: int, issue: IssueUpdate):
    with Session(engine) as session:
        try:
            res = session.query(Issue).filter(Issue.id == issue_id).first()
            if res:
                if issue.image_url is not None:
                    res.image_url = issue.image_url
                if issue.title_en is not None:
                    res.title_en = issue.title_en
                if issue.title_mn is not None:
                    res.title_mn = issue.title_mn
                if issue.title_tr is not None:
                    res.title_tr = issue.title_tr
                if issue.description_en is not None:
                    res.description_en = issue.description_en

                if issue.description_mn is not None:
                    res.description_mn = issue.description_mn
                if issue.description_tr is not None:
                    res.description_tr = issue.description_tr
                session.commit()
                session.refresh(res)
                return res
            else:
                return {"error_message": "Issue not found"}
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            return {"error_message": "Update execution error"}



# def delete_issue(volume_id:int):
#     with Session(engine) as session:
#         try:
#             res = session.query(Volume).filter(Volume.id == volume_id).first()
#             if res:
#                 session.delete(res)
#                 session.commit()
#             if res is None:
#                 raise HTTPException(
#                 status_code=404,
#                 detail=f"Volume with ID {volume_id} not found"
#             )
#             return res
#         except SQLAlchemyError as exc:
#             session.rollback()
#             print(exc)
#             return {"Error_message" : "Delete execution error"}