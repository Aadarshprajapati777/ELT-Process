from app.core.logging_config import logger

def process_file(file):
    logger.info(f"Processing file: {file.filename}")

    logger.info(f"Completed processing for file: {file.filename}")
