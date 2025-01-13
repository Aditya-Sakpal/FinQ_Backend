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