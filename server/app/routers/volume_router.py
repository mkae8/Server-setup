from fastapi import APIRouter
from controllers.volume.volume_controller import (get_all_volumes, get_volume_by_id,create_volume,update_volume,delete_volume)
from schemas.volume.volume_schemas import VolumeCreate, VolumeUpdate, ResponseVolume


volumeRouter = APIRouter()

@volumeRouter.get("/volumes")
def fetch_volumes():
    return get_all_volumes()

@volumeRouter.get("/volume/{volume_id}")
def fetch_volume(volume_id:int):
    return get_volume_by_id(volume_id)

@volumeRouter.post("/volume", response_model=ResponseVolume, status_code=201)
def add_volume(volume: VolumeCreate):
    return create_volume(volume)

@volumeRouter.put("/volumes/{volume_id}")
def modify_volume(volume_id:int, volume:VolumeUpdate):
    return update_volume(volume_id, volume)

@volumeRouter.delete("/volumes/{volumes_id}")
def remove_volume(volume_id:int):
    return delete_volume(volume_id)

    
    