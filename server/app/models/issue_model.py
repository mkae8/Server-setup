# from database import Base
# from sqlalchemy import Column, String, Integer, TIMESTAMP, func, ForeignKey
# from sqlalchemy.orm import relationship

# class Issue(Base):
#     __tablename__ = "issues"
    
#     id = Column(Integer, primary_key=True, nullable=False)
#     volume_id = Column(Integer, ForeignKey("volumes.id"), nullable=False)
#     title_en = Column(String, nullable=False)
#     title_mn = Column(String, nullable=False)
#     title_tr = Column(String, nullable=False)
#     image_url = Column(String, nullable=False)
#     description_en = Column(String, nullable=False)
#     description_mn = Column(String, nullable=False)
#     description_tr = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

#     volume = relationship("Volume", back_populates="issues")