from pydantic import BaseModel, validator

class FileSchema(BaseModel):
    filename: str
    content_type: str
    size: int

    @validator("filename")
    def validate_filename(cls, v):
        if not v.endswith((".csv", ".xlsx")):
            raise ValueError("Invalid file extension.")
        return v

    @validator("size")
    def validate_size(cls, v):
        if v > 10 * 1024 * 1024:  # 10 MB limit
            raise ValueError("File size exceeds the maximum limit.")
        return v
