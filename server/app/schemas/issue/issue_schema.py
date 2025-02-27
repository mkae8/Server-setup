from pydantic import BaseModel, Field
from typing import Optional


class IssueBase(BaseModel):
    volume_id: int
    title_en: str
    title_mn: str
    title_tr: str
    image_url: str  
    description_en: str
    description_mn: str
    description_tr: str


class IssueCreate(IssueBase):
    pass

class IssueUpdate(BaseModel):
    title_en: Optional[str] = None  
    title_mn: Optional[str] = None  
    title_tr: Optional[str] = None
    image_url: Optional[str] = None
    description_en: Optional[str] = None
    description_mn: Optional[str] = None
    description_tr: Optional[str] = None

class ResponseIssue(BaseModel):
    volume_id: int = Field(..., example=1)
    title_en: str = Field(..., example="Example")
    title_mn: str = Field(..., example="Жишээ")
    title_tr: str = Field(..., example="Örnek")
    image_url: str  = Field(..., example="http://placeholder.img")
    description_en: str = Field(..., example="Example")
    description_mn: str = Field(..., example="Жишээ")
    description_tr: str = Field(..., example="Örnek")