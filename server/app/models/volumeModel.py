from database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, func

class Volume(Base):
    __tablename__ = "volumes"
    id = Column(Integer, primary_key=True, nullable=False)
    volume_year = Column(String, nullable=False)
    volume_no = Column(String, nullable=False)
    title_en = Column(String, nullable=False)
    title_mn = Column(String, nullable=False)
    title_tr = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)