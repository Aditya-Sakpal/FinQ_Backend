from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict, Any


class HttpRequest(BaseModel):
    client_ip: str
    user_agent: str


class EventAttributes(BaseModel):
    http_request: HttpRequest


class Organization(BaseModel):
    admin_delete_enabled: Optional[bool]
    created_at: int
    created_by: Optional[str]
    has_image: Optional[bool]
    id: str
    image_url: Optional[HttpUrl]
    logo_url: Optional[HttpUrl]
    max_allowed_memberships: Optional[int]
    members_count: Optional[int]
    name: str
    object: str
    pending_invitations_count: Optional[int]
    public_metadata: Dict[str, Any]
    slug: str
    updated_at: int


class PublicUserData(BaseModel):
    first_name: Optional[str]
    has_image: Optional[bool]
    identifier: str
    image_url: Optional[HttpUrl]
    last_name: Optional[str]
    profile_image_url: Optional[HttpUrl]
    user_id: str


class OrganizationMembershipData(BaseModel):
    created_at: int
    id: str
    object: str
    organization: Organization
    public_user_data: PublicUserData
    role: str
    updated_at: int


class RemoveUserFromOrganizationRequest(BaseModel):
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


class AddUserToOrganizationRequest(BaseModel):
    data: OrganizationMembershipData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str


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