import logging

from fastapi import  Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions
from clerk_backend_api import Clerk

from app.utils.credentials import CLERK_SECRET_KEY
from app.utils.constants import CLERK_ALLOWED_PARTIES

logger = logging.getLogger(__name__)

clerk_client = Clerk(bearer_auth=CLERK_SECRET_KEY)
class ClerkAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        excluded_paths = ["/api/v1/create_user", "/api/v1/create_organization"]
        
        if request.url.path in excluded_paths:
            logger.info(f"Skipping ClerkAuthMiddleware for {request.url.path}")
            return await call_next(request)
        
        request_body = await request.body()
        logger.info(f"Incoming request headers: {request.headers}, request body: {request_body}")
        try:
            request_state = clerk_client.authenticate_request(
                request,
                AuthenticateRequestOptions(
                    authorized_parties=CLERK_ALLOWED_PARTIES
                )
            )
            if not request_state.is_signed_in:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Unauthorized access"}
                )
            request.state.user = request_state.user
        except Exception:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or expired token"}
            )

        response = await call_next(request)
        return response