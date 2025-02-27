from pydantic import BaseModel, Field
from typing import Optional




class VolumeBase(BaseModel):
    volume_year: int
    volume_no: int
    title_en: str
    title_mn: str
    title_tr: str

class VolumeCreate(VolumeBase):
    pass

class VolumeUpdate(BaseModel):
    volume_year: Optional[int] = None
    volume_no: Optional[int] = None
    title_en: Optional[str] = None
    title_mn: Optional[str] = None
    title_tr: Optional[str] = None

class ResponseVolume(BaseModel):
    volume_year: int = Field(..., example=2024)
    volume_no: int = Field(..., example=1)
    title_en: str = Field(..., example="Expamle")
    title_mn: str = Field(..., example="Жишээ")
    title_tr: str = Field(..., example="Örnek")
