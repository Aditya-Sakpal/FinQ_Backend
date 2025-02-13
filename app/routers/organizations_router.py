from datetime import datetime , timezone
import traceback

from fastapi import APIRouter , Request
from fastapi.responses import JSONResponse

from app.schemas.organizations_schema import CreateOrganizationRequest, DeleteOrganizationRequest , UpdateOrganizationRequest , RemoveUserFromOrganizationRequest
from app.crud.organizations_crud import *

router = APIRouter()

@router.post("/create_organization")
async def create_new_organization_api(request:CreateOrganizationRequest):
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
        
        response = create_organization(
            user_id=user_id,
            organization_id=organization_id,
            organization_name=organization_name,
            address=address,
            date_created=date_created,
            last_accessed=last_accessed,
            subscription_plan=subscription_plan
        )
        
        if 'error' in response:
            logger.error(f"Error creating organization: {response['error']}")
            return JSONResponse(content={"error":f"Error creating organization : {response['error']}"}, status_code=400)
        
        logging.info(f"Organization created: {organization_id}")
        return JSONResponse(content={"data":f"Organization created successfully : {organization_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error creating organization: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while creating organization : {e}"}, status_code=500)
    
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
            return JSONResponse(content={"error":f"Error retrieving organizations : {response['error']}"}, status_code=400)
        
        logger.info(f"Organizations retrieved successfully: {response.data}")
        return JSONResponse(content={"data":response}, status_code=200)
    except Exception as e:
        logger.error(f"Error retrieving organizations: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while retrieving organizations : {e}"}, status_code=500)
    
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
            return JSONResponse(content={"error":f"Error retrieving organization : {response['error']}"}, status_code=400)
        
        logging.info(f"Organization retrieved: {organization_id}")
        return JSONResponse(content={"data":response}, status_code=200)
    except Exception as e:
        logger.error(f"Error retrieving organization: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while retrieving organization : {e}"}, status_code=500)
    
@router.post("/update_organization")
async def update_organization_api(request:UpdateOrganizationRequest):
    """
    This function updates an organization in the Organizations table.
    
    Args:
    - request (UpdateOrganizationRequest): The request object containing the organization data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        request = request.data

        logger.info(f"Updating organization: {request}")
        
        organization_id = request.id
        organization_name = request.name
        date_created = datetime.fromtimestamp(request.created_at / 1000, tz=timezone.utc).isoformat()
        last_accessed = datetime.fromtimestamp(request.updated_at / 1000, tz=timezone.utc).isoformat()
        
        response = update_organization(
            organization_id=organization_id,
            organization_name=organization_name,
            date_created=date_created,
            last_accessed=last_accessed,
        )
        
        if 'error' in response:
            logger.error(f"Error updating organization: {response['error']}")
            return JSONResponse(content={"error":f"Error updating organization : {response['error']}"}, status_code=400)
        
        logging.info(f"Organization updated: {organization_id}")
        return JSONResponse(content={"data":f"Organization updated successfully : {organization_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error updating organization: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while updating organization : {e}"}, status_code=500)
    
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
        logger.info(f"Deleting organization: {request}")
        old_organization_id = request.data.id
        
        response = delete_organization(
            old_organization_id=old_organization_id,
        )
        
        if 'error' in response:
            logger.error(f"Error deleting organization: {response['error']}")
            return JSONResponse(content={"error":f"Error deleting organization : {response['error']}"}, status_code=400)
        
        logger.info(f"Organization deleted successfully: {old_organization_id}")
        return JSONResponse(content={"data":f"Organization deleted successfully : {old_organization_id}"}, status_code=200)            
    except Exception as e:
        logger.error(f"Error deleting organization: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while deleting organization : {e}"}, status_code=500)  
    
@router.post("/add_user_to_organization")
async def add_user_to_organization_api(request: Request):
    """
    This function adds a user to an organization in the Organizations table.    
    
    Args:
    - request (Request): The request object containing the organization membership data.
    
    Returns:
    - JSONResponse: The response indicating the outcome of the operation.
    """
    try:
        request_data = await request.json()  # Parse the JSON body from the request
        logger.info(f"Adding user to organization: {request_data}")
        
        # Extract necessary fields with fallback for missing keys
        new_organization_id = request_data.get('data').get("organization", {}).get("id")
        user_id = request_data.get('data').get("public_user_data", {}).get("user_id")
        
        if not new_organization_id or not user_id:
            return JSONResponse(
                content={"error": "Missing required fields: 'organization.id' or 'public_user_data.user_id'"},
                status_code=400,
            )
        
        response = add_user_to_organization(
            new_organization_id=new_organization_id,
            user_id=user_id,
        )
        
        if 'error' in response:
            logger.error(f"Error updating user: {response['error']}")
            return JSONResponse(content={"error": f"Error updating user: {response['error']}"}, status_code=400)
        
        logger.info(f"User added to organization successfully: {user_id}")
        return JSONResponse(content={"data": "User added to organization successfully"}, status_code=200)
    
    except Exception as e:
        logger.error(f"Error adding user to organization: {traceback.format_exc()}")
        return JSONResponse(content={"error": f"Error while adding user to organization: {e}"}, status_code=500)

@router.post("/remove_user_from_organization")
async def remove_user_from_organization_api(request: Request):
    """
    This function removes a user from an organization in the Organizations table.
    
    Args:
    - request (Request): The request object containing the organization membership data.
    
    Returns:
    - JSONResponse: The response indicating the outcome of the operation.
    """
    try:
        request_data = await request.json()  
        logger.info(f"Removing user from organization: {request_data}")
        
        organization_id = request_data.get('data').get("organization", {}).get("id")
        user_id = request_data.get('data').get("public_user_data", {}).get("user_id")
        
        if not organization_id or not user_id:
            return JSONResponse(
                content={"error": "Missing required fields: 'organization.id' or 'public_user_data.user_id'"},
                status_code=400,
            )
        
        response = remove_user_from_organization(
            organization_id=organization_id,
            user_id=user_id,
        )
        
        if 'error' in response:
            logger.error(f"Error removing user from organization: {response['error']}")
            return JSONResponse(content={"error": f"Error removing user from organization: {response['error']}"}, status_code=400)
        
        logger.info(f"User removed from organization successfully: {user_id}")
        return JSONResponse(content={"data": "User removed from organization successfully"}, status_code=200)
    
    except Exception as e:
        logger.error(f"Error removing user from organization: {traceback.format_exc()}")
        return JSONResponse(content={"error": f"Error while removing user from organization: {e}"}, status_code = 500)