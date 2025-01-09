from app.db.connect import supabase

def upload_new_company_document(
    file_id:str,
    user_id:str,
    organization_id:str,
    file_type:str,
    file_uri:str,
    file_size:int,
    file_name:str,
    status:str,
    company_id:str,
    company_name:str,
    company_description:str,
    primary_operating_country:str,
    primary_listing_country:str,
    is_custom_created:bool,
    created_by:str,
    industry:str,
    sector:str,
    year:int,
    type:str,
    company_document_id:str
):
    try:
        return supabase.rpc("new_company_upload", {
            "p_file_id": file_id,
            "p_user_id": user_id,
            "p_organization_id": organization_id,
            "p_file_type": file_type,
            "p_file_uri": file_uri,
            "p_file_size": file_size,
            "p_file_name": file_name,
            "p_status": status,
            "p_company_id": company_id,
            "p_company_name": company_name,
            "p_company_description": company_description,
            "p_primary_operating_country": primary_operating_country,
            "p_primary_listing_country": primary_listing_country,
            "p_is_custom_created": is_custom_created,
            "p_created_by": created_by,
            "p_industry": industry,
            "p_sector": sector,
            "p_year": year,
            "p_type": type,
            "p_company_document_id": company_document_id
        }).execute()
    except Exception as e:
        return {"message": "Error uploading new company document", "error": str(e)}
    
def get_files():
    """
    This function retrieves all files from the Files table.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").select("*").execute()
        return response
    except Exception as e:
        return {"message": "Error getting files", "error": str(e)}
    
def get_file_by_file_id(file_id:str):
    """
    This function retrieves a file from the files table by its ID.

    Args:
    - file_id (str): The file's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").select("*").eq("file_id", file_id).execute()
        return response
    except Exception as e:
        return {"message": "Error getting file", "error": str(e)}
    
def get_files_by_user_id(user_id:str):
    """
    This function retrieves a file from the files table by its user ID.

    Args:
    - user_id (str): The user's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").select("*").eq("user_id", user_id).execute()
        return response
    except Exception as e:
        return {"message": "Error getting file", "error": str(e)}
    
def get_files_by_organization_id(organization_id:str):
    """
    This function retrieves a file from the files table by its organization ID.

    Args:
    - organization_id (str): The organization's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").select("*").eq("organization_id", organization_id).execute()
        return response
    except Exception as e:
        return {"message": "Error getting file", "error": str(e)}
    
def update_file(file_id:str, update_data:dict):
    """
    Updates a file in the files table with the specified fields.

    Args:
    - file_id (str): The file's ID.
    - update_data (dict): A dictionary containing the fields to update and their new values.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        if not update_data:
            raise ValueError("No data provided to update.")

        response = supabase.table("Files").update(update_data).eq("file_id", file_id).execute()
        return response
    except Exception as e:
        return {"message": "Error updating file", "error": str(e)}
    
def delete_file(file_id:str):
    """
    Deletes a file from the files table.

    Args:
    - file_id (str): The file's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").delete().eq("file_id", file_id).execute()
        return response
    except Exception as e:
        return {"message": "Error deleting file", "error": str(e)}