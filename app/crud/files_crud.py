from app.db.connect import supabase
    
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