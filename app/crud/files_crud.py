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

def upload_existing_company_document(
    user_id:str,
    organization_id:str,
    file_id:str,
    file_type:str,
    file_size:str,
    file_uri:str,
    file_name:str,
    status:str,
    company_id:str,
    company_document_id:str,
    year:str,
    type:str
):
    try:
        return supabase.rpc("existing_company_upload", {
            "p_user_id": user_id,
            "p_organization_id": organization_id,
            "p_file_id": file_id,
            "p_file_type": file_type,
            "p_file_size": file_size,
            "p_file_uri": file_uri,
            "p_file_name": file_name,
            "p_status": status,
            "p_company_id": company_id,
            "p_company_document_id": company_document_id,
            "p_created_by": user_id,
            "p_year": year,
            "p_type": type
        }).execute()
    except Exception as e:
        return {"message": "Error uploading existing company document", "error": str(e)}  
    
def get_files():
    """
    This function retrieves all files from the Files table.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        return supabase.table("Files").select("*").execute()
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
        return supabase.table("Files").select("*").eq("file_id", file_id).execute()
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
        return supabase.table("Files").select("*").eq("user_id", user_id).execute()
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
        return supabase.table("Files").select("*").eq("organization_id", organization_id).execute()
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

        return supabase.table("Files").update(update_data).eq("file_id", file_id).execute()
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
        return supabase.table("Files").delete().eq("file_id", file_id).execute()
    except Exception as e:
        return {"message": "Error deleting file", "error": str(e)}
    
def upload_new_format(
    user_id:str,
    organization_id:str,
    file_id:str,
    file_type:str,
    file_uri:str,
    file_size:int,
    file_name:str,
    format_id:str,
    format_name:str,
    format_description:str,
    format_category:str,
    status:str,
):
    """
    Uploads a new format to the Formats table.
    
    Args:
    - user_id (str): The user's ID.
    - organization_id (str): The organization's ID.
    - file_id (str): The file's ID.
    - file_type (str): The file's type.
    - file_uri (str): The file's URI.
    - file_size (int): The file's size.
    - file_name (str): The file's name.
    - format_id (str): The format's ID.
    - format_name (str): The format's name.
    - format_description (str): The format's description.
    - format_category (str): The format's category.
    - status (str): The status of the format.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        return supabase.rpc("upload_new_format", {
            "p_user_id": user_id,
            "p_organization_id": organization_id,
            "p_file_id": file_id,
            "p_file_type": file_type,
            "p_file_uri": file_uri,
            "p_file_size": file_size,
            "p_file_name": file_name,
            "p_format_id": format_id,
            "p_format_name": format_name,
            "p_format_description": format_description,
            "p_format_category": format_category,
            "p_status": status,
        }).execute()
    except Exception as e:
        return {"message": "Error uploading new format", "error": str(e)}

def get_companies_documents(
    id: str,
):
    """
    This function retrieves all companies documents from the Company_Documents table.
    
    Args:
    - id (str): The organization's ID or user's ID .

    Returns:
    - dict: The response from the Supabase API. 
    """
    try:
        return supabase.rpc("fetch_company_documents", {
            "p_id": id,
        }).execute()
    except Exception as e:
        return {"message": "Error getting companies documents", "error": str(e)}