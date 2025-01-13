import logging
import traceback
import uuid

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.formats_schema import UploadNewFormatRequest
from app.crud.formats_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()
    
  
@router.post("/upload_new_format")
async def upload_new_format_api(request:UploadNewFormatRequest):
    """
    This function uploads a new format to the formats table.
    
    Args:
    - request (UploadNewFormatRequest): The request object.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        format_id = "format_"+str(uuid.uuid4())
        file_id = "file_"+str(uuid.uuid4())
        
        response = upload_new_format(
            user_id = request.user_id,
            organization_id = request.organization_id,
            file_id = file_id,
            file_type = request.file_type,
            file_uri = request.file_uri,
            file_size = request.file_size,
            file_name = request.file_name,
            format_id = format_id,
            format_name = request.format_name,
            format_description = request.format_description,
            format_category = request.format_category,
            status='pending'
        )
        
        if 'error' in response:
            logger.error(f"Error uploading new format: {response['error']}")
            return JSONResponse(content={"error":f"Error uploading new format : {response['error']}"}, status_code=400)
        
        logging.info(f"New format uploaded: {format_id}")
        return JSONResponse(content={"data": f"New format uploaded : {format_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error uploading new format: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while uploading new format : {e}"}, status_code=500)