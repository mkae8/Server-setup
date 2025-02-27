from database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship

class Volume(Base):
    __tablename__ = "volumes"
    
    id = Column(Integer, primary_key=True, nullable=False)
    volume_year = Column(String, nullable=False)
    volume_no = Column(String, nullable=False)
    title_en = Column(String, nullable=False)
    title_mn = Column(String, nullable=False)
    title_tr = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    issues = relationship("Issue", back_populates="volume")

class Issue(Base):
    __tablename__ = "issues"
    
    id = Column(Integer, primary_key=True, nullable=False)
    volume_id = Column(Integer, ForeignKey("volumes.id"), nullable=False)
    title_en = Column(String, nullable=False)
    title_mn = Column(String, nullable=False)
    title_tr = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    description_en = Column(String, nullable=False)
    description_mn = Column(String, nullable=False)
    description_tr = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    volume = relationship("Volume", back_populates="issues")
    editors = relationship("Editor", back_populates="issue")
    categories = relationship("Category", back_populates="issue")

class Editor(Base):
    __tablename__ = "editors"
    
    id = Column(Integer, primary_key=True, nullable=False)
    issue_id = Column(Integer, ForeignKey("issues.id"), nullable=False)

    firstname_en = Column(String, nullable=False)
    firstname_mn = Column(String, nullable=False)
    firstname_tr = Column(String, nullable=False)

    middlename_en = Column(String, nullable=True)
    middlename_mn = Column(String, nullable=True)
    middlename_tr = Column(String, nullable=True)

    lastname_en = Column(String, nullable=False)
    lastname_mn = Column(String, nullable=False)
    lastname_tr = Column(String, nullable=False)

    role_en = Column(String, nullable=False)
    role_mn = Column(String, nullable=False)
    role_tr = Column(String, nullable=False)

    suffix_en = Column(String, nullable=False)
    suffix_mn = Column(String, nullable=False)
    suffix_tr = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    
    issue = relationship("Issue", back_populates="editors")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, nullable=False)
    issue_id = Column(Integer, ForeignKey("issues.id"), nullable=False)
    title_en = Column(String, nullable=False)
    title_mn = Column(String, nullable=False)
    title_tr = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    issue = relationship("Issue", back_populates="categories")
    articles = relationship("Article", back_populates="category")

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    file_url = Column(String, nullable=False)
    title_en = Column(String, nullable=False)
    title_mn = Column(String, nullable=False)
    title_tr = Column(String, nullable=False)
    placement_begin = Column(Integer, nullable=False)
    placement_end = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    category = relationship("Category", back_populates="articles")
    authors = relationship("Author", back_populates="article")

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)

    firstname_en = Column(String, nullable=False)
    firstname_mn = Column(String, nullable=False)
    firstname_tr = Column(String, nullable=False)

    lastname_en = Column(String, nullable=False)
    lastname_mn = Column(String, nullable=False)
    lastname_tr = Column(String, nullable=False)

    middlename_en = Column(String, nullable=False)
    middlename_mn = Column(String, nullable=False)
    middlename_tr = Column(String, nullable=False)

    suffix_en = Column(String, nullable=False)
    suffix_mn = Column(String, nullable=False)
    suffix_tr = Column(String, nullable=False)
    
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    article = relationship("Article", back_populates="authors")