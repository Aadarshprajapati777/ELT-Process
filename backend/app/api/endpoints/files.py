from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import List
from app.schemas.file_schemas import FileSchema
from app.api.services.validation import validate_files
from app.api.services.elt_process import process_file
from app.core.logging_config import logger

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the ELT application."}

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    processed_files = []

    for file in files:
        try:
            # Read file info
            file_info = FileSchema(
                filename=file.filename,
                content_type=file.content_type,
                size=len(await file.read())
            )
            
            
            file.file.seek(0)

            validate_files(files)

            process_file(file)

            processed_files.append(file_info)
        
        except HTTPException as e:
            logger.error(f"Error processing file {file.filename}: {e.detail}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error with file {file.filename}: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred.")

    return {"detail": "Files uploaded and processed successfully.", "files": processed_files}
