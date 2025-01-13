import traceback
import logging

from app.db.connect import supabase

logger = logging.getLogger(__name__)


def update_plan(
    transaction_id: str,
    user_id:str,
    organization_id: str,
    details: dict,
    status: str,
):
    try :
        return supabase.rpc("update_plan",{
            "p_transaction_id": transaction_id,
            "p_user_id": user_id,
            "p_organization_id": organization_id,
            "p_details": details,
            "p_status": status,
        }).execute()
    except Exception as e:
        logger.error(f"Error inserting transaction: {traceback.format_exc()}")
        return {"message": "Error inserting transaction", "error": str(e)}

def get_transaction(
    transaction_id: str,
):
    """
    This function retrieves a transaction from the Transactions table.
    
    Args:
    - transaction_id (int): The transaction's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Transactions").select("*").eq("transaction_id", transaction_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error getting transaction: {traceback.format_exc()}")
        return {"message": "Error getting transaction", "error": str(e)}
    
def get_transactions_of_an_organization(
    organization_id: str,
):
    """
    This function retrieves all transactions of a specific organization from the Transactions table.
    
    Args:
    - organization_id (int): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Transactions").select("*").eq("organization_id", organization_id).execute()
        return response
    except Exception as e:
        logger.error(f"Error getting transactions of an organization: {traceback.format_exc()}")
        return {"message": "Error getting transactions of an organization", "error": str(e)}