import logging
import traceback
import uuid

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.company_documents_schema import UploadNewCompanyDocumentRequest,UploadExistingCompanyDocumentRequest
from app.crud.company_documents_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/upload_file_for_new_company")
def upload_file_api(request: UploadNewCompanyDocumentRequest):
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
            user_id=request.user_id,
            organization_id=request.organization_id,
            file_type=request.file_type,
            file_size=request.file_size,
            file_uri=request.file_uri,
            file_name=request.file_name,
            status="pending",
            company_id=company_id,
            company_name=request.company_name,
            company_description="",
            primary_listing_country="India",
            primary_operating_country="India",
            is_custom_created=True,
            created_by=request.user_id,
            industry="",
            sector="",
            year=request.year,
            type=request.type,
            company_document_id=company_document_id
        )
        
        if 'error' in response:
            logger.error(f"Error creating company document: {response['error']}")
            return JSONResponse(content={"error":f"Error creating company document : {response['error']}"}, status_code=400)
        
        logging.info(f"Company document created file id: {file_id}")
        return JSONResponse(content={"data": f"Company document created file id : {file_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error uploading file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while uploading file : {e}"}, status_code=500)
    
@router.post("/upload_file_for_existing_company")
def upload_file_for_existing_company_api(request: UploadExistingCompanyDocumentRequest):
    """
    This function creates a new file in the files table.
    
    Args:
    - file (FileUploadRequest): The file to create.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        file_id = "file_"+str(uuid.uuid4())
        company_document_id = "company_document_"+str(uuid.uuid4())
        
        response = upload_existing_company_document(
            user_id=request.user_id,
            organization_id=request.organization_id,
            file_id=file_id,
            file_type=request.file_type,
            file_size=request.file_size,
            file_uri=request.file_uri,
            file_name=request.file_name,
            status="pending",
            company_id=request.company_id,
            company_document_id=company_document_id,
            year=request.year,
            type=request.type
        )
        
        if 'error' in response:
            logger.error(f"Error creating company document: {response['error']}")
            return JSONResponse(content={"error":f"Error creating company document : {response['error']}"}, status_code=400)
        
        logging.info(f"Company document created file id: {file_id}")
        return JSONResponse(content={"data": f"Company document created file id : {file_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error uploading file: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while uploading file : {e}"}, status_code=500)
    
@router.get("/get_companies_documents/{id}")
async def get_companies_documents_api(id:str):
    """
    This function retrieves all company documents from the CompaniesDocuments table.
    
    Args:
    - id (str): It could be organization_id or user_id.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_companies_documents(id)
        
        if 'error' in response:
            logger.error(f"Error getting company documents: {response['error']}")
            return JSONResponse(content={"error":f"Error retrieving company documents : {response['error']}"}, status_code=400)
        
        logging.info(f"Company documents retrieved: {response}")
        return response
    except Exception as e:
        logger.error(f"Error getting company documents: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error retrieving company documents : {e}"}, status_code=500)