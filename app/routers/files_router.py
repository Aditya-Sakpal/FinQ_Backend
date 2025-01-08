import logging
import traceback
import uuid

from fastapi import APIRouter, Response

from app.schemas.files_schema import FileUploadRequest
from app.crud.files_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/upload_file_for_new_company")
def upload_file_api(file: FileUploadRequest):
    """
    This function creates a new file in the files table.
    
    Args:
    - file (FileUploadRequest): The file to create.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        file_id = "file_"+str(uuid.uuid4())
        company_id = "company_"+str(uuid.uuid4())
        company_document_id = "company_document_"+str(uuid.uuid4())
        
        response = upload_new_company_document(
            file_id=file_id,
            user_id=file.user_id,
            organization_id=file.organization_id,
            file_type=file.file_type,
            file_size=file.file_size,
            file_uri=file.file_uri,
            file_name=file.file_name,
            status="pending",
            company_id=company_id,
            company_name=file.company_name,
            company_description="",
            primary_listing_country="India",
            primary_operating_country="India",
            is_custom_created=True,
            created_by=file.user_id,
            industry="",
            sector="",
            year=file.year,
            type=file.type,
            company_document_id=company_document_id
        )
        
        if 'error' in response:
            logger.error(f"Error creating company document: {response['error']}")
            return Response(content=f"Error creating company document : {response['error']}", status_code=400)
        
        logging.info(f"Company document created: {response}")
        
        return response
        
    except Exception as e:
        logger.error(f"Error uploading file: {traceback.format_exc()}")
        return Response(content=f"Error while uploading file : {e}", status_code=500)
    
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
            return Response(content=f"Error retrieving files : {response['error']}", status_code=400)
        
        logging.info(f"Files retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting files: {traceback.format_exc()}")
        return Response(content=f"Error while retrieving files : {e}", status_code=500)
    
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
            return Response(content=f"Error retrieving file by file id : {response['error']}", status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return Response(content=f"Error while retreiving file by file id : {e}", status_code=500)
    
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
            return Response(content=f"Error while retreiving file by user id : {response['error']}", status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return Response(content=f"Error while retreiving file by user id : {e}", status_code=500)
    
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
            return Response(content=f"Error while retreiving file by organization id : {response['error']}", status_code=400)
        
        logging.info(f"file retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting file: {traceback.format_exc()}")
        return Response(content=f"Error while retreiving file by organization id : {e}", status_code=500)
    
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
            return Response(content=f"Error updating file : {response['error']}", status_code=400)
        
        logging.info(f"file updated: {response}")
        return response
    except Exception as e:
        logger.error(f"Error updating file: {traceback.format_exc()}")
        return Response(content=f"Error while updating file : {e}", status_code=500)
    
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
            return Response(content=f"Error deleting file : {response['error']}", status_code=400)
        
        logging.info(f"file deleted: {response}")
        return response
    except Exception as e:
        logger.error(f"Error deleting file: {traceback.format_exc()}")
        return Response(content=f"Error while while file : {e}", status_code=500)
