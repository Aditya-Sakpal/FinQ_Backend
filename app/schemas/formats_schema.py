from pydantic import BaseModel

class UploadNewFormatRequest(BaseModel):
    user_id: str
    organization_id: str
    file_type:str
    file_uri:str
    file_size:int
    file_name:str
    format_name:str
    format_description:str
    format_category:str