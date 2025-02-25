from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from models.volumeModel import Volume
from schemas.volume.volume_schemas import VolumeCreate, VolumeUpdate ,VolumeBase
from fastapi import HTTPException
from typing import Optional


def get_all_volumes():
     with Session(engine) as session:
          try:
               result = session.query(Volume).all()
               return result
          except SQLAlchemyError as exc:
               print(f"Database error: {exc}")
               return{"Error_message":"Get execution error"}
          
def get_volume_by_id(volume_id: int):
    with Session(engine) as session:
        try:
            result = session.query(Volume).filter(Volume.id == volume_id).first()
            if result is None:
                raise HTTPException(
                status_code=404,
                detail=f"Volume with ID {volume_id} not found"
            )
            return result
        except SQLAlchemyError as exc:
            print(f"Database error: {exc}")
            return{"Error_message": "Get execution error"}  

def create_volume(volume_year : str, volume_no:str, title_en:str, title_mn:str, title_tr:str):
    with Session(engine) as session:
        try:
            res = VolumeCreate(volume_year=volume_year, volume_no=volume_no, title_en=title_en, title_mn=title_mn, title_tr=title_tr )
            session.add(res)
            session.commit()
            session.refresh(res)
            return res
        except SQLAlchemyError as exc:
                session.rollback()
                print(exc)
                return {"error_message": "Insert execution error"}
        
def update_volume(
    volume_id: int,
    volume_year: Optional[str] = None,
    volume_no: Optional[str] = None,
    title_en: Optional[str] = None,
    title_mn: Optional[str] = None,
    title_tr: Optional[str] = None
):
    with Session(engine) as session:
        try:
            result = session.query(VolumeUpdate).filter(VolumeUpdate.id == volume_id).first()
            if result:
                if volume_year is not None:
                    setattr(result, "volume_year", volume_year)
                if volume_no is not None:
                    setattr(result, "volume_no", volume_no)
                if title_en is not None:
                    setattr(result, "title_en", title_en)
                if title_mn is not None:
                    setattr(result, "title_mn", title_mn)
                if title_tr is not None:
                    setattr(result, "title_tr", title_tr)
                
                session.commit()
                session.refresh(result)
                return result
            else:
                raise HTTPException(status_code=404, detail="Volume not found")
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            raise HTTPException(status_code=500, detail="Update execution error")
        
def delete_volume(volume_id:int):
    with Session(engine) as session:
        try:
            res = session.query(Volume).filter(Volume.id == volume_id).first()
            if res:
                session.delete(res)
                session.commit()
            return res
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            return {"Error_message" : "Delete execution error"}