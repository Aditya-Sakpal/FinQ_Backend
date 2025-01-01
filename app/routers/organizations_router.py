import logging
from datetime import datetime , timezone
import traceback

from fastapi import APIRouter , Response

from app.schemas.organizations_schema import CreateOrganizationRequest
from app.crud.organizations_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/create_organization")
async def create_organization_api(request: CreateOrganizationRequest):
    """
    This function creates a new organization in the Organizations table.
    
    Args:
    - request (CreateOrganizationRequest): The request object containing the organization data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        request = request.data
        
        logger.info(f"Creating organization: {request}")
        
        organization_id = request.id
        organization_name = request.name
        address = ''
        date_created = datetime.fromtimestamp(request.created_at / 1000, tz=timezone.utc).isoformat()
        last_accessed = datetime.fromtimestamp(request.updated_at / 1000, tz=timezone.utc).isoformat()
        subscription_plan = 'basic'
        
        response = create_organization(
            organization_id=organization_id,
            organization_name=organization_name,
            address=address,
            date_created=date_created,
            last_accessed=last_accessed,
            subscription_plan=subscription_plan,
        )
        
        if 'error' in response:
            logger.error(f"Error creating organization: {response['error']}")
            return Response(content=f"Error creating organization : {response['error']}", status_code=400)
            
        return {"message": "Organization created successfully", "data": response} 
    except Exception as e:
        logger.error(f"Error creating organization: {traceback.format_exc()}")
        return Response(content=f"Error while creating organization : {e}", status_code=500)
    
@router.get("/get_organizations")
async def get_organizations_api():
    """
    This function retrieves all organizations from the Organizations table.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_organizations()
        
        if 'error' in response:
            logger.error(f"Error retrieving organizations: {response['error']}")
            return Response(content=f"Error retrieving organizations : {response['error']}", status_code=400)
        
        return response
    except Exception as e:
        logger.error(f"Error retrieving organizations: {traceback.format_exc()}")
        return Response(content=f"Error while retrieving organizations : {e}", status_code=500)
    
@router.get("/get_organization/{organization_id}")
async def get_organization_api(organization_id: str):
    """
    This function retrieves an organization from the Organizations table.
    
    Args:
    - organization_id (int): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_organization(organization_id)
        
        if 'error' in response:
            logger.error(f"Error retrieving organization: {response['error']}")
            return Response(content=f"Error retrieving organization : {response['error']}", status_code=400)
        
        return response
    except Exception as e:
        logger.error(f"Error retrieving organization: {traceback.format_exc()}")
        return Response(content=f"Error while retrieving organization : {e}", status_code=500)