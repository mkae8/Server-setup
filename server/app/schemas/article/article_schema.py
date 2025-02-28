from pydantic import BaseModel, Field
from typing import Optional

class ArticleBase(BaseModel):
    category_id : int
    file_url : str
    title_en : str
    title_mn : str
    title_tr : str
    placement_begin : int
    placement_end : int

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    file_url : Optional[str] = None
    title_en : Optional[str] = None
    title_mn : Optional[str] = None
    title_tr : Optional[str] = None
    placement_begin : Optional[int] = None
    placement_end : Optional[int] = None


class ArticleResponse(BaseModel):
    category_id : int = Field(..., example=1)
    file_url : str = Field(..., example="http://placeholder.file")
    title_en : str = Field(..., example="Table of Contents")
    title_mn : str = Field(..., example="Агуулга")
    title_tr : str = Field(..., example="İçindekiler")
    placement_begin : int = Field(..., example=1)
    placement_end : int = Field(..., example=4)