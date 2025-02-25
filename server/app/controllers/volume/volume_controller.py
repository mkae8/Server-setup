from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine
from models.volumeModel import Volume
from schemas.volume.volume_schemas import VolumeCreate, VolumeUpdate
from fastapi import HTTPException



def get_all_volumes():
     with Session(engine) as session:
          try:
               result = session.query(Volume).all()
               print("resultresultresultresultresult")
               print(result)
               print("resultresultresultresultresult")
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
            res = Volume(**volume.model_dump())  
            session.add(res)
            session.commit()
            session.refresh(res)
            return res
        except SQLAlchemyError as exc:
            session.rollback()
            print(exc)
            return {"error_message": "Insert execution error"}

        
def update_volume(volume_id: int, volume: VolumeUpdate):
    with Session(engine) as session:
        try:
            result = session.query(Volume).filter(Volume.id == volume_id).first()
            if result:
                for key, value in volume.model_dump(exclude_unset=True).items():
                    setattr(result, key, value)
                
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