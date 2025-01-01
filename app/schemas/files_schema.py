from pydantic import BaseModel

class FileUploadRequest(BaseModel):
    file_id: str
    user_id: str
    organization_id: str
    uploaded_on: str
    file_type: str
    file_uri: str
    file_size : int
    file_name : str