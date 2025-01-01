from app.db.connect import supabase

def upload_file(
    file_id: str,
    user_id: str,
    organization_id: str,
    uploaded_on: str,
    file_type: str,
    file_uri: str,
    file_size : int,
    file_name : str,
):
    """
    This function uploads a file to the Files table.
    
    Args:
    - file_id (str): The file's ID.
    - user_id (str): The user's ID.
    - organization_id (str): The organization's ID.
    - uploaded_on (str): The date the file was uploaded.
    - file_type (str): The file's type.
    - file_uri (str): The file's URI.
    - file_size (int): The file's size.
    - file_name (str): The file's name.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        files_data = {
            "file_id": file_id,
            "user_id": user_id,
            "organization_id": organization_id,
            "uploaded_on": uploaded_on,
            "file_type": file_type,
            "file_uri": file_uri,
            "file_size": file_size,
            "file_name": file_name,
        }
        response = supabase.table("Files").insert(files_data).execute()
        return response
    except Exception as e:
        return {"message": "Error uploading file", "error": str(e)}
    
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
    
def get_file_by_user_id(user_id:str):
    """
    This function retrieves a file from the files table by its user ID.

    Args:
    - user_id (str): The user's ID.

    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Files").select("*").eq("file_owner", user_id).execute()
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