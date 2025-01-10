import traceback

from fastapi import APIRouter , Response
from app.crud.transactions_crud import *

router = APIRouter()

@router.get("/get_transaction/{transaction_id}")
async def get_transaction_api(transaction_id: str):
    """
    This function retrieves a transaction from the Transactions table.
    
    Args:
    - transaction_id (int): The transaction's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_transaction(transaction_id)
        
        if 'error' in response:
            logger.error(f"Error retrieving transaction: {response['error']}")
            return Response(content=f"Error retrieving transaction : {response['error']}", status_code=400)
        
        logging.info(f"Transaction retrieved successfully: {transaction_id}")
        return response
    except Exception as e:
        logger.error(f"Error retrieving transaction: {traceback.format_exc()}")
        return Response(content=f"Error while retrieving transaction : {e}", status_code=500)
    
@router.get("/get_transactions_of_an_organization/{organization_id}")
async def get_transactions_of_an_organization_api(organization_id: str):
    """
    This function retrieves all transactions of a specific organization from the Transactions table.
    
    Args:
    - organization_id (int): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_transactions_of_an_organization(organization_id)
        
        if 'error' in response:
            logger.error(f"Error retrieving transactions of an organization: {response['error']}")
            return Response(content=f"Error retrieving transactions of an organization : {response['error']}", status_code=400)
        
        logging.info(f"Transactions of an organization retrieved successfully: {organization_id}")
        return response
    except Exception as e:
        logger.error(f"Error retrieving transactions of an organization: {traceback.format_exc()}")
        return Response(content=f"Error while retrieving transactions of an organization : {e}", status_code=500)