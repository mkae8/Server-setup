from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    issue_id : int
    title_en : str
    title_mn : str
    title_tr : str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title_en: Optional[str] = None
    title_mn: Optional[str] = None
    title_tr: Optional[str] = None

class CategoryResponse(BaseModel):
    issue_id : int = Field(..., example=1)
    title_en : str = Field(..., example="Example")
    title_mn : str = Field(..., example="Жишээ")
    title_tr : str = Field(..., example="Örnek")
