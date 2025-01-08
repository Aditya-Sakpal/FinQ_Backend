from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional, Union

class Verification(BaseModel):
    status: str
    strategy: str
    attempts: Optional[Union[int, None]] = None
    expire_at: Optional[Union[int, None]] = None

class EmailAddress(BaseModel):
    email_address: EmailStr
    id: str
    linked_to: List[dict]
    object: str
    reserved: Optional[bool] = None
    verification: Verification

class HTTPRequest(BaseModel):
    client_ip: str
    user_agent: str

class EventAttributes(BaseModel):
    http_request: HTTPRequest

class UserData(BaseModel):
    birthday: Optional[str] = None
    created_at: int
    email_addresses: List[EmailAddress]
    external_accounts: List[dict]
    external_id: Optional[Union[str, None]] = None
    first_name: str
    gender: Optional[str] = None
    id: str
    image_url: HttpUrl
    last_name: Optional[str] = None
    last_sign_in_at: Optional[Union[int, None]] = None
    object: str
    password_enabled: bool
    phone_numbers: List[dict]
    primary_email_address_id: str
    primary_phone_number_id: Optional[Union[str, None]] = None
    primary_web3_wallet_id: Optional[Union[str, None]] = None
    private_metadata: dict
    profile_image_url: HttpUrl
    public_metadata: dict
    two_factor_enabled: bool
    unsafe_metadata: dict
    updated_at: int
    username: Optional[Union[str, None]] = None
    web3_wallets: List[dict]

class CreateUserRequest(BaseModel):
    data: UserData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str

class UpdateUserRequest(BaseModel):
    data: UserData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str

class DeleteUserData(BaseModel):
    deleted: bool
    id: str
    object: str

class DeleteUserRequest(BaseModel):
    data: DeleteUserData
    event_attributes: EventAttributes
    object: str
    timestamp: int
    type: str
