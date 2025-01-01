from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

class HttpRequest(BaseModel):
    client_ip: str
    user_agent: str

class EventAttributes(BaseModel):
    http_request: HttpRequest

class OrganizationData(BaseModel):
    created_at: int
    created_by: str
    id: str
    image_url: Optional[HttpUrl]
    logo_url: Optional[HttpUrl]
    name: str
    object: str
    public_metadata: Dict[str, Any]
    slug: str
    updated_at: int

class CreateOrganizationRequest(BaseModel):
    data: OrganizationData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str