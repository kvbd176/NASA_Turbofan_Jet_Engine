from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from auth.dependencies import get_current_user
import os


router = APIRouter()


UPLOAD_DIR = "uploads"


@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )


    user_folder = os.path.join(
        UPLOAD_DIR,
        f"user_{current_user.id}"
    )


    os.makedirs(
        user_folder,
        exist_ok=True
    )


    file_path = os.path.join(
        user_folder,
        file.filename
    )


    content = await file.read()


    if len(content) == 0:
        raise HTTPException(
            status_code=400,
            detail="Empty file uploaded"
        )


    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(content)


    return {

        "status": "SUCCESS",

        "message": "Dataset uploaded",

        "user_id": current_user.id,

        "file_name": file.filename,

        "file_path": file_path
    }