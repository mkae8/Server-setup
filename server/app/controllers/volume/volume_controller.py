from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from models.volumeModel import Volume
from schemas.volume.volume_schemas import VolumeCreate, VolumeUpdate, ResponseVolume
from fastapi import HTTPException



def get_all_volumes():
     with Session(engine) as session:
          try:
               result = session.query(Volume).all()
               print("Query Result:", result)
               return result
               
          except SQLAlchemyError as exc:
               print(f"Database error: {exc}")
               raise HTTPException(status_code=500, detail="Database error")

          
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

def create_volume(volume: VolumeCreate):
    with Session(engine) as session:
        try:

            result = Volume(
                volume_year=volume.volume_year,
                volume_no=volume.volume_no,
                title_en=volume.title_en,
                title_mn=volume.title_mn,
                title_tr=volume.title_tr
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
def update_volume(volume_id: int, volume: VolumeUpdate):
    with Session(engine) as session:
        try:
            res = session.query(Volume).filter(Volume.id == volume_id).first()
            if res:
                if volume.volume_year is not None:
                    res.volume_year = volume.volume_year
                if volume.volume_no is not None:
                    res.volume_no = volume.volume_no
                if volume.title_en is not None:
                    res.title_en = volume.title_en
                if volume.title_mn is not None:
                    res.title_mn = volume.title_mn
                if volume.title_tr is not None:
                    res.title_tr = volume.title_tr
                session.commit()
                session.refresh(res)
                return res
            else:
                return {"error_message": "Volume not found"}
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            return {"error_message": "Update execution error"}



def delete_volume(volume_id:int):
    with Session(engine) as session:
        try:
            res = session.query(Volume).filter(Volume.id == volume_id).first()
            if res:
                session.delete(res)
                session.commit()
            if res is None:
                raise HTTPException(
                status_code=404,
                detail=f"Volume with ID {volume_id} not found"
            )
            return res
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            return {"Error_message" : "Delete execution error"}