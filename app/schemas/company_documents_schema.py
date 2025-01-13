from pydantic import BaseModel

class UploadNewCompanyDocumentRequest(BaseModel):
    file_name: str
    file_type: str
    file_size: int
    file_uri: str
    user_id: str
    organization_id: str
    company_name : str
    year : int
    type : str

class UploadExistingCompanyDocumentRequest(BaseModel):
    file_name: str
    file_type: str
    file_size: int
    file_uri: str
    user_id: str
    organization_id: str
    company_id:str
    year : int
    type : str