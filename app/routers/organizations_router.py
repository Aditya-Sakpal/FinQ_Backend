import logging
from datetime import datetime , timezone
import traceback
import uuid

from fastapi import APIRouter , Response

from app.schemas.organizations_schema import CreateOrganizationRequest , AddUserToOrganizationRequest , DeleteOrganizationRequest
from app.crud.organizations_crud import *
from app.crud.users_crud import update_user , get_user

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
        user_id = request.created_by
        address = ''
        date_created = datetime.fromtimestamp(request.created_at / 1000, tz=timezone.utc).isoformat()
        last_accessed = datetime.fromtimestamp(request.updated_at / 1000, tz=timezone.utc).isoformat()
        subscription_plan = 'basic'
        
        response = get_user(user_id)
        
        if 'error' in response:
            logger.error(f"Error getting user: {response['error']}")
            return Response(content=f"Error retrieving user : {response['error']}", status_code=400)
        
        organization_to_be_deleted = response['data'][0]['organization_id']
        
        response = delete_organization(organization_to_be_deleted)
        
        if 'error' in response:
            logger.error(f"Error deleting organization: {response['error']}")
            return Response(content=f"Error deleting organization : {response['error']}", status_code=400)
        
        response = create_organization(
            organization_id=organization_id,
            user_id=user_id,
            organization_name=organization_name,
            address=address,
            date_created=date_created,
            last_accessed=last_accessed,
            subscription_plan=subscription_plan,
        )
        
        if 'error' in response:
            logger.error(f"Error creating organization: {response['error']}")
            return Response(content=f"Error creating organization : {response['error']}", status_code=400)
        
        response = update_user(user_id, {"organization_id": organization_id, "role": 'owner'})
        
        if 'error' in response:
            logger.error(f"Error updating user: {response['error']}")
            return Response(content=f"Error updating user : {response['error']}", status_code=400)
            
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

    
@router.post("/delete_organization")
async def delete_organization_api(request:DeleteOrganizationRequest):
    """
    This function deletes an organization from the Organizations table.
    
    Args:
    - request (DeleteOrganizationRequest): The request object containing the organization data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try :
        timestamp = request.timestamp
        request = request.data
        logger.info(f"Deleting organization: {request}")
        response = get_organization(organization_id)
        
        if 'error' in response:
            logger.error(f"Error getting organization: {response['error']}")
            return Response(content=f"Error retrieving organization : {response['error']}", status_code=400)
        
        user_id = response['data'][0]['user_id']
        
        organization_id = request.organization.id
        response = delete_organization(organization_id)
        
        if 'error' in response:
            logger.error(f"Error deleting organization: {response['error']}")
            return Response(content=f"Error deleting organization : {response['error']}", status_code=400)
        
        response = create_organization(
            organization_id=str(uuid.uuid4()),
            user_id=user_id,
            organization_name=f"{user_id}_puesdo_org",
            address=None,
            date_created=datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).isoformat() ,
            last_accessed= datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).isoformat(),
            subscription_plan='basic',
        )
        
        return {"message": "Organization deleted successfully", "data": response}
    except Exception as e:
        logger.error(f"Error deleting organization: {traceback.format_exc()}")
        return Response(content=f"Error while deleting organization : {e}", status_code=500)    
    
@router.post("/add_user_to_organization")
async def add_user_to_organization_api(request:AddUserToOrganizationRequest):
    """
    This function adds a user to an organization in the Organizations table.    
    
    Args:
    - request (AddUserToOrganizationRequest): The request object containing the organization membership data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        request = request.data
        logger.info(f"Adding user to organization: {request}")
        organization_id = request.organization.id
        user_id = request.public_user_data.user_id
        response = get_user(user_id)
        
        if 'error' in response:
            logger.error(f"Error getting user: {response['error']}")
            return Response(content=f"Error retrieving user : {response['error']}", status_code=400)
        
        organization_to_be_deleted = response['data'][0]['organization_id']
        response = delete_organization(organization_to_be_deleted)

        if 'error' in response:
            logger.error(f"Error deleting user from organization: {response['error']}")
            return Response(content=f"Error deleting user from organization : {response['error']}", status_code=400)
        
        response = update_user(user_id, {"organization_id": organization_id, "role": request.role})
        
        if 'error' in response:
            logger.error(f"Error updating user: {response['error']}")
            return Response(content=f"Error updating user : {response['error']}", status_code=400)
        
        return {"message": "User added to organization successfully", "data": response}
    except Exception as e:
        logger.error(f"Error adding user to organization: {traceback.format_exc()}")
        return Response(content=f"Error while adding user to organization : {e}",   status_code=500)