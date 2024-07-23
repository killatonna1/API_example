from fastapi import APIRouter, UploadFile
import shutil

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Upload image"]
)

@router.post("/upload_image")
async def add_image(name: str, file: UploadFile):
    im_path = f"app/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)