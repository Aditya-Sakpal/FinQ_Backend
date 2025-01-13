from app.db.connect import supabase

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