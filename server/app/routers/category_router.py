from fastapi import APIRouter
from controllers.category.category_controller import (get_all_categories, create_category, update_category) 
from schemas.category.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse

categoryRouter = APIRouter()

@categoryRouter.get("/catogory")
def fetch_categories():
    return get_all_categories()

@categoryRouter.post("/category", response_model=CategoryResponse, status_code=201)
def add_category(category:CategoryCreate):
    return create_category(category)

@categoryRouter.put("/category/{category_id}", response_model=CategoryResponse)
def modify_category( category_id:int ,category:CategoryUpdate):
    return update_category(category_id, category)

