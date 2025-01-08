from pydantic import BaseModel

class FileUploadRequest(BaseModel):
    file_name: str
    file_type: str
    file_size: int
    file_uri: str
    user_id: str
    organization_id: str
    company_name : str
    year : int
    type : str