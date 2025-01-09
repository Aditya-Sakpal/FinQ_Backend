import logging
from datetime import datetime , timezone
import traceback
import uuid

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.users_schema import CreateUserRequest , UpdateUserRequest , DeleteUserRequest
from app.crud.users_crud import *

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/create_user")
async def create_user_api(request: CreateUserRequest):
    """
    This function creates a new user in the Users table.
    
    Args:
    - request (CreateUserRequest): The request object containing the user data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        request = request.data
        user_id = request.id
        organization_id = "org_"+str(uuid.uuid4())
        username = request.username or None  
        first_name = request.first_name
        last_name = request.last_name
        email_address = request.email_addresses[0].email_address if request.email_addresses else None
        phone_number = request.phone_numbers[0] if request.phone_numbers else None 
        address = None  
        account_type = 'individual'
        date_created = datetime.fromtimestamp(request.created_at / 1000, tz=timezone.utc).isoformat()  
        last_accessed = datetime.fromtimestamp(request.updated_at / 1000, tz=timezone.utc).isoformat()          
        organization_role = 'owner' 
        organization_name = f"{user_id}_puesdo_org" 
        subscription_plan = 'basic'
        
        response = create_user(
            user_id=user_id,
            organization_id=organization_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            address=address,
            account_type=account_type,
            subscription_plan=subscription_plan,
            date_created=date_created,
            last_accessed=last_accessed,
            organization_role=organization_role,
            organization_name=organization_name,
        )
        
        if 'error' in response:
            logger.error(f"Error creating user: {response['error']}")
            return JSONResponse(content={"error":f"Error creating user : {response['error']}"}, status_code=400)
        
        logger.info(f"User created successfully: {user_id}")
        return JSONResponse(content={"data": f"User created successfully : {user_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error creating user: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error while creating user : {e} "}, status_code=500)
    
    
@router.get("/get_users")
async def get_users_api():
    """
    This function retrieves all users from the Users table.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_users()
        
        if 'error' in response:
            logger.error(f"Error getting users: {response['error']}")
            return JSONResponse(content={"error":f"Error retrieving users : {response['error']}"}, status_code=400)
        
        logger.info(f"Users retrieved successfully: {response.data}")
        return JSONResponse(content={"data": response.data}, status_code=200)
    except Exception as e:
        logger.error(f"Error getting users: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error retrieving users : {e}"}, status_code=500)
    
@router.get("/get_user/{user_id}")
async def get_user_api(user_id: str):
    """
    This function retrieves a user from the Users table by user_id.
    
    Args:
    - user_id (str): The user's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_user(user_id)
        
        if 'error' in response:
            logger.error(f"Error getting user: {response['error']}")
            return JSONResponse(content={"error":f"Error retrieving user : {response['error']}"}, status_code=400)
        
        logger.info(f"User retrieved successfully: {response.data}")
        return JSONResponse(content={"data": response.data}, status_code=200)
    except Exception as e:
        logger.error(f"Error getting user: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error retrieving user : {e}"}, status_code=500)
    
@router.put("/update_user")
async def update_user_api(request: UpdateUserRequest):
    """
    This function updates a user in the Users table.
    
    Args:
    - request (UpdateUserRequest): The request object containing the update data.
    
    Returns:
    - dict: The response from the Supabase API.
    """    
    try :
        request = request.data
        user_id = request.id
        username = request.username or None  
        first_name = request.first_name
        last_name = request.last_name
        email_address = request.email_addresses[0].email_address if request.email_addresses else None
        phone_number = request.phone_numbers[0] if request.phone_numbers else None 
        date_created = datetime.fromtimestamp(request.created_at / 1000, tz=timezone.utc).isoformat()  
        last_accessed = datetime.fromtimestamp(request.updated_at / 1000, tz=timezone.utc).isoformat()          
          
        response = update_user(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            date_created=date_created,
            last_accessed=last_accessed,
        )   
        
        if 'error' in response:
            logger.error(f"Error updating user: {response['error']}")
            return JSONResponse(content={"error":f"Error updating user : {response['error']}"}, status_code=400)
        
        logger.info(f"User updated successfully: {response.data}")
        return JSONResponse(content={"data":f"User updated successfully: {user_id   }"}, status_code=200)    
    except Exception as e:
        logger.error(f"Error updating user: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error updating user : {e}"}, status_code=500)
    
@router.delete("/delete_user")
async def delete_user_api(request: DeleteUserRequest):
    """
    This function deletes a user from the Users table.
    
    Args:
    - request (DeleteUserRequest): The request object containing the user data.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try :
        request = request.data 
        user_id = request.id
        response = delete_user(user_id)
        
        if 'error' in response:
            logger.error(f"Error deleting user: {response['error']}")
            return JSONResponse(content={"error":f"Error deleting user : {response['error']}"}, status_code=400)
        
        logger.info(f"User deleted successfully: {response.data}")
        return JSONResponse(content={"data":f"User deleted successfully: {user_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error deleting user: {traceback.format_exc()}")
        return JSONResponse(content={"error":f"Error deleting user : {e}"}, status_code=500)