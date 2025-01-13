from pydantic import BaseModel

class UpdatePlanRequest(BaseModel):
    organization_id: str
    user_id: str
    amount: str
    currency: str
    changes_in_n_queries_per_month: int
    change_in_max_companies_per_query: int
    change_in_custom_documents_number_limit: int
    change_in_custom_documents_size_limit: int
    change_in_max_custom_companies: int
    change_in_max_custom_formats: int
    change_in_max_members: int