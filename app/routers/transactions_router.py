import traceback
import uuid

from fastapi import APIRouter 
from fastapi.responses import JSONResponse
from app.crud.transactions_crud import *
from app.schemas.transaction_schema import UpdatePlanRequest

router = APIRouter()

@router.post("/update_plan")
async def update_plan_api(request: UpdatePlanRequest):
    """
    This function updates a transaction in the Transactions table.
    
    Args:
    - request (UpdatePlanRequest): The request body.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        transaction_id = "transaction_"+str(uuid.uuid4())
        details = {
            "amount": request.amount,
            "currency": request.currency,
            "changes_in_n_queries_per_month": request.changes_in_n_queries_per_month,
            "change_in_max_companies_per_query": request.change_in_max_companies_per_query,
            "change_in_custom_documents_number_limit": request.change_in_custom_documents_number_limit,
            "change_in_custom_documents_size_limit": request.change_in_custom_documents_size_limit,
            "change_in_max_custom_companies": request.change_in_max_custom_companies,
            "change_in_max_custom_formats": request.change_in_max_custom_formats,
            "change_in_max_members": request.change_in_max_members,
        }
        response = update_plan(
            transaction_id,
            request.user_id,
            request.organization_id,
            details,
            "completed",
        )
        
        if 'error' in response:
            logger.error(f"Error updating transaction: {response['error']}")
            return JSONResponse(content={"error": response['error']}, status_code=400)
        
        logging.info(f"Transaction updated successfully: {transaction_id}")
        return JSONResponse(content={"data": f"Transaction updated successfully {transaction_id}"}, status_code=200)
    except Exception as e:
        logger.error(f"Error updating transaction: {traceback.format_exc()}")
        return JSONResponse(content={"error": f"Error while updating transaction : {e}"}, status_code=500)

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
            return JSONResponse(content={"error": f"Error retrieving transaction : {response['error']}"}, status_code=400)
        
        logging.info(f"Transaction retrieved successfully: {transaction_id}")
        return response
    except Exception as e:
        logger.error(f"Error retrieving transaction: {traceback.format_exc()}")
        return JSONResponse(content={"error": f"Error while retrieving transaction : {e}"}, status_code=500)

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
            return JSONResponse(content={"error": f"Error retrieving transactions of an organization : {response['error']}"}, status_code=400)
        
        logging.info(f"Transactions of an organization retrieved successfully: {organization_id}")
        return response
    except Exception as e:
        logger.error(f"Error retrieving transactions of an organization: {traceback.format_exc()}")
        return JSONResponse(content={"error": f"Error while retrieving transactions of an organization : {e}"}, status_code=500)