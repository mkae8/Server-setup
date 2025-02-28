from fastapi import APIRouter
from controllers.editor.editor_controller import (get_all_editors, get_editor_by_id, create_editor, update_editor )
from schemas.editor.editor_schema import EditorCreate, EditorResponse, EditorUpdate

editorRouter= APIRouter()

@editorRouter.get("/editor")
def fetch_editors():
    return get_all_editors()

@editorRouter.get("/editor/{editor_id}", response_model=EditorResponse)
def fetch_editor_by_id(editor_id:int):
    return get_editor_by_id(editor_id)

@editorRouter.post("/editor", response_model=EditorResponse, status_code=201)
def add_editor(editor:EditorCreate):
    return create_editor(editor)

@editorRouter.put("/editor/{editor_id}", response_model=EditorUpdate)
def modify_editor(editor_id : int, editor:EditorUpdate):
    return update_editor(editor_id, editor)