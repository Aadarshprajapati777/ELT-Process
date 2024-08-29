import filetype
from fastapi import UploadFile, HTTPException
from app.exceptions.custom_exceptions import InvalidFileTypeException, FileTooLargeException

def validate_files(files):
    for file in files:
        file_content = file.file.read()
        
        # Check if the file is a CSV
        if file.filename.endswith('.csv'):
            if not file_content.startswith(b'\xEF\xBB\xBF') and b',' not in file_content:
                raise InvalidFileTypeException(f"File {file.filename} doesn't seem to be a valid CSV.")
        
        # Check if the file is an XLSX
        elif file.filename.endswith('.xlsx'):
            kind = filetype.guess(file_content)
            if kind is None or kind.mime != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                raise InvalidFileTypeException(f"Invalid MIME type for file {file.filename}. Expected XLSX.")
        
        # If the file has an unsupported extension
        else:
            raise InvalidFileTypeException(f"Unsupported file type for file {file.filename}. Only CSV and XLSX files are allowed.")
        
        # Check file size
        if len(file_content) > 10 * 1024 * 1024:  # 10 MB limit
            raise FileTooLargeException(f"File {file.filename} is too large. Max size is 10 MB.")
        
        # Reset file pointer after reading
        file.file.seek(0)
