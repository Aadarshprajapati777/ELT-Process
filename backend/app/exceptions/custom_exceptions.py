from fastapi import HTTPException, status
# app/exceptions/custom_exceptions.py

class InvalidFileTypeException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class FileTooLargeException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File is too large.")
