import logging
import traceback

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.crud.files_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()
    
@router.get("/get_files")
async def get_all_files_api():
    """
    This function retrieves all files from the Files table.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_files()
        
        if 'error' in response:
            logger.error(f"Error getting files: {response['error']}")
            return JSONResponse(content={"error":f"Error retrieving files : {response['error']}"}, status_code=400)
        
        logging.info(f"Files retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting files: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error retrieving files : {e}"}, status_code=500)
    
@router.get("/get_file_by_file_id/{file_id}")
async def get_file_by_id_api(file_id: str):
    """
    This function retrieves a file from the files table by its ID.
    
    Args:
    - file_id (str): The file's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_file_by_file_id(file_id)
        
        if 'error' in response:
            logger.error(f"Error getting file: {response['error']}")
            return JSONResponse(content={"data":f"Error while retreiving file by file id : {response['error']}"}, status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while retreiving file by file id : {e}"}, status_code=500)
    
@router.get("/get_files_by_user_id/{user_id}")
async def get_files_by_user_id_api(user_id: str):
    """
    This function retrieves a file from the files table by its user ID.
    
    Args:
    - user_id (str): The user's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_files_by_user_id(user_id)
        
        if 'error' in response:
            logger.error(f"Error getting file: {response['error']}")
            return JSONResponse(content={"error":f"Error while retreiving file by user id : {response['error']}"}, status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while retreiving file by user id : {e}"}, status_code=500)
    
@router.get("/get_files_by_organization_id/{organization_id}")
async def get_files_by_organization_id_api(organization_id: str):
    """
    This function retrieves a file from the files table by its organization ID.
    
    Args:
    - organization_id (str): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_files_by_organization_id(organization_id)
        
        if 'error' in response:
            logger.error(f"Error getting file: {response['error']}")
            return JSONResponse(content={"error":f"Error while retreiving file by organization id : {response['error']}"}, status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while retreiving file by organization id : {e}"}, status_code=500)
    
@router.put("/update_file/{file_id}")
async def update_file_api(file_id: str, update_data: dict):
    """
    This function updates a file in the files table.
    
    Args:
    - file_id (str): The file's ID.
    - update_data (dict): The data to update.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = update_file(file_id, update_data)
        
        if 'error' in response:
            logger.error(f"Error updating file: {response['error']}")
            return JSONResponse(content={"error":f"Error while updating file : {response['error']}"}, status_code=400)
        
        logging.info(f"file updated: {response}")
        return JSONResponse(content={"data": f"File updated : {response}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error updating file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while updating file : {e}"}, status_code=500)

@router.get("/delete_file/{file_id}")
async def delete_file_api(file_id: str):
    """
    This function deletes a file from the files table.
    
    Args:
    - file_id (str): The file's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = delete_file(file_id)
        
        if 'error' in response:
            logger.error(f"Error deleting file: {response['error']}")
            return JSONResponse(content={"error":f"Error while while file : {response['error']}"}, status_code=400)
            
        logging.info(f"file deleted: {response}")
        return JSONResponse(content={"data": f"File deleted : {response}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error deleting file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while deleting file : {e}"}, status_code=500)
 