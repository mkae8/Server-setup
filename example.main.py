# @app.post("/user")
# def create_user_data(username : str, age:int):
#     with Session(engine) as session:
#         try:
#             res = User(username=username, age=age)
#             session.add(res)
#             session.commit()
#             session.refresh(res)
#             return res
#         except SQLAlchemyError as exc:
#                 session.rollback()
#                 print(exc)
#                 return {"error_message": "Insert execution error"}
        

# @app.get("/users")
# def fetch_users_data():
#     with Session(engine) as session:
#         try:
#             result = session.query(User).all()
#             return result
#         except SQLAlchemyError as exc:
#                 print(exc)
#                 return {"error_message": "Get execution error"}




        
# @app.put("/user")
# def update_user_data(user_id:int, username:str):
#     with Session(engine) as session:
#         try:
#             res = session.query(User).filter(User.id == user_id).first()
#             if res:
#                  setattr(res, "username", username)
#                  session.commit()
#                  session.refresh(res)
#             return res
#         except SQLAlchemyError as exc:
#                 session.rollback()
#                 print(exc)
#                 return {"error_message": "Update execution error"}


# @app.delete("/user")
# def delete_user(user_id:int):
#     with Session(engine) as session:
#         try:
#             res = session.query(User).filter(User.id == user_id).first()
#             if res:
#                  session.delete(res)
#                  session.commit()
#             return res
#         except SQLAlchemyError as exc:
#                 session.rollback()
#                 print(exc)
#                 return {"error_message": "Delete execution error"}


# @app.get("/volume/{volume_id}")
# def fetch_volume_data_by_id(volume_id: int, db: Session = Depends(get_db)):
#     try:
#         # Fetch the volume by ID
#         result = db.query(Volume).filter(Volume.id == volume_id).first()
        
#         # If no volume is found, raise a 404 error
#         if result is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail=f"Volume with ID {volume_id} not found"
#             )
        
#         # Return the volume data
#         return result
#     except SQLAlchemyError as exc:
#         # Log the error and return a 500 error
#         print(f"Database error: {exc}")
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Database error"
#         )


# @app.get("/")
# def root_read():
#     return {"message" : "Hello world"}
