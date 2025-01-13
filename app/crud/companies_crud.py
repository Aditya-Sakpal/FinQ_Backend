from app.db.connect import supabase

def create_company(
    company_id:str,
    organization_id:str,
    created_by:str,
    company_name:str,
    company_description:str,
    primary_listing_country:str,
    primary_operating_country:str,
    is_custom_created:bool,
    created_at:str,
    industry:str,
    sector:str
):
    """
    This function creates a new company in the Companies table.
    
    Args:
    - company_id (str): The company's ID.
    - organization_id (str): The organization's ID.
    - created_by (str): The user's ID.
    - company_name (str): The company's name.
    - company_description (str): The company's description.
    - primary_listing_country (str): The company's primary listing country.
    - primary_operating_country (str): The company's primary operating country.
    - is_custom_created (bool): Whether the company was custom created.
    - created_at (str): The date the company was created.
    - industry (str): The company's industry.
    - sector (str): The company's sector.
    
    Returns:
    - dict: The response from the Supabase API.
    """
    try:
        response = supabase.table("Companies").insert(
            {
                "company_id": company_id,
                "organization_id": organization_id,
                "created_by": created_by,
                "company_name": company_name,
                "company_description": company_description,
                "primary_listing_country": primary_listing_country,
                "primary_operating_country": primary_operating_country,
                "is_custom_created": is_custom_created,
                "created_at": created_at,
                "industry": industry,
                "sector": sector
            }
        ).execute()
        return response 
    except Exception as e:
        return {"message": "Error creating company", "error": str(e)}
    
def get_companies(
    id:str
):
    try:
        return supabase.rpc("fetch_companies",{
            "p_id": id
        }).execute()
    except Exception as e:
        return {"message": "Error getting companies", "error": str(e)}