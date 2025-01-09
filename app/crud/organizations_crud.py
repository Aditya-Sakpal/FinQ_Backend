import traceback
import logging

from app.db.connect import supabase

logger = logging.getLogger(__name__)


def create_organization(
    user_id: str,
    organization_id:str,
    organization_name:str,
    address:str,
    date_created:str,
    last_accessed:str,
    subscription_plan:str,
):
    """
    This function creates a new organization in the Organizations table.
    
    Args:
    - user_id (str): The user's ID.
    - organization_id (str): The organization's ID.
    - organization_name (str): The organization's name.
    - address (str): The organization's address.
    - date_created (str): The date the organization was created.
    - last_accessed (str): The last time the organization accessed the application.
    - subscription_plan (str): The organization's subscription plan.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        return supabase.rpc("create_new_organization", {
            "p_user_id": user_id, 
            "p_organization_id": organization_id, 
            "p_organization_name": organization_name, 
            "p_address": address, 
            "p_date_created": date_created, 
            "p_last_accessed": last_accessed, 
            "p_subscription_plan": subscription_plan
        }).execute()
    except Exception as e:
        logger.error(f"Error creating organization: {traceback.format_exc()}")
        return {"message": "Error creating organization", "error": str(e)}
    
def get_organizations():
    """
    This function retrieves all organizations from the Organizations table.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Organizations").select("*").execute()
        return response
    except Exception as e:
        logger.error(f"Error getting organizations: {traceback.format_exc()}")
        return {"message": "Error getting organizations", "error": str(e)}
    
def get_organization(organization_id: int):
    """
    This function retrieves an organization from the Organizations table by organization_id.
    
    Args:
    - organization_id (int): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Organizations").select("*").eq("organization_id", organization_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error getting organization: {traceback.format_exc()}")
        return {"message": "Error getting organization", "error": str(e)}
    
def add_user_to_organization(
    user_id:str,
    new_organization_id:str
):
    """
    This function adds a user to an organization in the Organizations table.
    
    Args:
    - user_id (str): The user's ID.
    - new_organization_id (str): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        return supabase.rpc("add_user_to_organization", {
            "p_user_id": user_id,
            "new_organization_id": new_organization_id
        }).execute()
    except Exception as e:
        logger.error(f"Error adding user to organization: {traceback.format_exc()}")
        return {"message": "Error adding user to organization", "error": str(e)}

def delete_organization(
        old_organization_id:str,
    ):
    """
    This function deletes an organization from the Organizations table. It also replaces the organization_id with a new one.
    
    Args:
    - old_organization_id (str): The old organization's ID.
    - new_organization_id (str): The new organization's ID.
    - timestampz (str): The timestamp of the deletion.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        return supabase.rpc("delete_organization", {
            "p_organization_id": old_organization_id,
        }).execute()
    except Exception as e:
        logger.error(f"Error deleting organization: {traceback.format_exc()}")
        return {"message": "Error deleting organization", "error": str(e)}