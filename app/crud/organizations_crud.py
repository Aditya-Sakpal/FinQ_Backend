import traceback
import logging

from app.db.connect import supabase

logger = logging.getLogger(__name__)

def create_organization(
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
    - organization_id (int): The organization's ID.
    - organization_name (str): The organization's name.
    - address (str): The organization's address.
    - date_created (str): The date the organization was created.
    - last_accessed (str): The last time the organization accessed the application.
    - subscription_plan (str): The organization's subscription plan.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        organization_data = {
            "organization_id": organization_id,
            "organization_name": organization_name,
            "address": address,
            "date_created": date_created,
            "last_accessed": last_accessed,
            "subscription_plan": subscription_plan,
        }
        response = supabase.table("Organizations").insert(organization_data).execute()
        return response
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