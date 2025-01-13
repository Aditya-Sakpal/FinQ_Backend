from fastapi import APIRouter 
from fastapi.responses import JSONResponse
from app.crud.companies_crud import *

router = APIRouter()

@router.get("/get_companies/{id}")
async def get_companies_api(id: str):
    """
    This function retrieves all companies of a specific organization from the Companies table.
    
    Args:
    - id (int): The organization's ID.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = get_companies(id)
        
        if 'error' in response:
            return JSONResponse(content={"error": response['error']}, status_code=400)
        
        return response
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
