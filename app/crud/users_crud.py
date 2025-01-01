import traceback
import logging
import uuid

from app.db.connect import supabase
from app.crud.organizations_crud import create_organization

logger = logging.getLogger(__name__)

def create_user(
    user_id:str,
    organization_id:str,
    username:str,
    first_name:str,
    last_name:str,
    email_address:str,
    phone_number:str,
    address:str,
    account_type:str,
    subscription_plan:str,
    date_created:str,
    last_accessed:str,
    organization_role:str,
    organization_name:str,
):
    """
        This function creates a new user in the Users table.

        Args:
        - user_id (int): The user's ID.
        - organization_id (int): The organization's ID.
        - username (str): The user's username.
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
        - email_address (str): The user's email address.
        - phone_number (str): The user's phone number.
        - address (str): The user's address.
        - account_type (str): The user's account type.
        - subscription_plan (str): The user's subscription plan.
        - date_created (str): The date the user was created.
        - last_accessed (str): The last time the user accessed the application.
        - organization_role (str): The user's role in the organization.
        - organization_name (str): The organization's name.

        Returns:
        - dict: The response from the Supabase API.
    """
    try:
        organization_response = create_organization(
            organization_id=organization_id,
            organization_name=organization_name,
            address=address,
            date_created=date_created,
            last_accessed=last_accessed,
            subscription_plan=subscription_plan,
        )
        
        if 'error' in organization_response:
            logger.error(f"Error creating organization: {organization_response['error']}")
            return organization_response
        
        user_data = {
            "user_id": user_id,
            "organization_id": organization_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "phone_number": phone_number,
            "address": address,
            "account_type": account_type,
            "date_created": date_created,
            "last_accessed": last_accessed,
            "organization_role": organization_role,
        }
        response = supabase.table("Users").insert(user_data).execute()
        return response
    except Exception as e:
        logger.error(f"Error inserting user: {traceback.format_exc()}")
        return {"error": str(e)}
    
def get_users():
    """
        This function retrieves all users from the Users table.

        Returns:
        - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Users").select("*").execute()
        return response
    except Exception as e:
        logger.error(f"Error retrieving users: {traceback.format_exc()}")
        return {"error": str(e)}
    
def get_user(user_id: int):
    """
        This function retrieves a user from the Users table.

        Args:
        - user_id (int): The user's ID.

        Returns:
        - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Users").select("*").eq("user_id", user_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error retrieving user: {traceback.format_exc()}")
        return {"error": str(e)}
    
def update_user(user_id: int, update_data: dict):
    """
    Updates a user in the Users table with the specified fields.

    Args:
    - user_id (int): The user's ID.
    - update_data (dict): A dictionary containing the fields to update and their new values.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        if not update_data:
            raise ValueError("No data provided to update.")

        response = supabase.table("Users").update(update_data).eq("user_id", user_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error updating user: {traceback.format_exc()}")
        return {"error": str(e)}

def delete_user(user_id: int):
    """
    Deletes a user from the Users table.

    Args:
    - user_id (int): The user's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Users").delete().eq("user_id", user_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error deleting user: {traceback.format_exc()}")
        return {"error": str(e)}