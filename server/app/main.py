from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine, Base
from dotenv import load_dotenv
from models.userModels import User
from models.volumeModel import Volume
from aws import AWS_Cognito, get_aws_cognito, SignUpModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/volume")
def fetch_volumes_datas():
     with Session(engine) as session:
          try:
               result = session.query(Volume).all()
               return result
          except SQLAlchemyError as exc:
               print(f"Database error: {exc}")
               return{"Error_message":"Get execution error"}
          
@app.get("/volume/{volume_id}")
def fetch_volume_data_by_id(volume_id: int):
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

@app.post("/volume")
def create_volume_data(volume_year : str, volume_no:str, title_en:str, title_mn:str, title_tr:str):
    with Session(engine) as session:
        try:
            res = Volume(volume_year=volume_year, volume_no=volume_no, title_en=title_en, title_mn=title_mn, title_tr=title_tr )
            session.add(res)
            session.commit()
            session.refresh(res)
            return res
        except SQLAlchemyError as exc:
                session.rollback()
                print(exc)
                return {"error_message": "Insert execution error"}
        
@app.put("/volume")
def update_volume_datas(
    volume_id: int,
    volume_year: Optional[str] = None,
    volume_no: Optional[str] = None,
    title_en: Optional[str] = None,
    title_mn: Optional[str] = None,
    title_tr: Optional[str] = None
):
    with Session(engine) as session:
        try:
            result = session.query(Volume).filter(Volume.id == volume_id).first()
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

@app.delete("/volume")
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
            
@app.post("/sign_up")
def sign_up(user: SignUpModel, cognito: AWS_Cognito = Depends(get_aws_cognito)):
     return cognito.sign_up(user)
          
