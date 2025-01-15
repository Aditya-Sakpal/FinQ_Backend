from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict, Any


class HttpRequest(BaseModel):
    client_ip: str
    user_agent: str


class EventAttributes(BaseModel):
    http_request: HttpRequest


class Organization(BaseModel):
    admin_delete_enabled: bool
    created_at: int
    created_by: Optional[str] 
    has_image: bool
    id: str
    image_url: Optional[HttpUrl]
    logo_url: Optional[HttpUrl]
    max_allowed_memberships: int
    members_count: int
    name: str
    object: str
    pending_invitations_count: int
    public_metadata: Dict[str, Any]
    slug: str
    updated_at: int


class PublicUserData(BaseModel):
    first_name: str
    has_image: bool
    identifier: str
    image_url: Optional[HttpUrl]
    last_name: str
    profile_image_url: Optional[HttpUrl]
    user_id: str


class OrganizationMembershipData(BaseModel):
    created_at: int
    id: str
    object: str
    organization: Organization
    permissions: List[str]
    public_metadata: Dict[str, Any]
    public_user_data: PublicUserData
    role: str
    role_name: str
    updated_at: int


class AddUserToOrganizationRequest(BaseModel):
    data: OrganizationMembershipData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str


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


class DeleteOrganizationData(BaseModel):
    deleted: bool
    id: str
    object: str


class DeleteOrganizationRequest(BaseModel):
    data: DeleteOrganizationData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str


class UpdateOrganizationRequest(BaseModel):
    data: OrganizationData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str
