from pydantic import BaseModel
from typing import Optional

class VolumeBase(BaseModel):
    volume_year: str
    volume_no: str
    title_en: str
    title_mn: str
    title_tr: str

class VolumeCreate(VolumeBase):
    pass

class VolumeUpdate(BaseModel):
    volume_year: Optional[str] = None
    volume_no: Optional[str] = None
    title_en: Optional[str] = None
    title_mn: Optional[str] = None
    title_tr: Optional[str] = None

class VolumesResponse(BaseModel):
    id: int
    volume_year: str
    volume_no: str
    title_en: str
    title_mn: str
    title_tr: str