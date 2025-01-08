from app.db.connect import supabase

def create_company_document(
    company_id:str,
    company_document_id:str,
    file_id:str,
    organization_id:str,
    year:int,
    type:str,
    time_tag:str,
    status:str
):
    """
    This function creates a new company document in the Company_Documents table.
    
    Args:
    - company_id (str): The company's ID.
    - company_document_id (str): The company document's ID.
    - file_id (str): The file's ID.
    - organization_id (str): The organization's ID.
    - year (int): The year the document was created.
    - type (str): The document's type.
    - time_tag (str): The time tag for the document.
    - status (str): The document's status.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Company_Documents").insert(
            {
                "company_id": company_id,
                "company_document_id": company_document_id,
                "file_id": file_id,
                "organization_id": organization_id,
                "year": year,
                "type": type,
                "time_tag": time_tag,
                "status": status
            }
        ).execute()
        return response 
    except Exception as e:
        return {"message": "Error creating company document", "error": str(e)}