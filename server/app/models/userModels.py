from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    username = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))




