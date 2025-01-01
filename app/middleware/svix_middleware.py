import logging
from svix import Webhook
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from credentials import CREATE_USER_WEBHOOK_SECRET, CREATE_ORGANIZATION_WEBHOOK_SECRET

logger = logging.getLogger(__name__)

class SvixWebhookAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        webhook_paths = ["/api/v1/create_user", "/api/v1/create_organization"]

        if request.url.path in webhook_paths:
            logger.info(f"Authenticating webhook for {request.url.path}")

            body = await request.body()
            payloadString = body.decode("utf-8")  
            svixHeaders = {
                "svix-id": request.headers.get("svix-id"),
                "svix-timestamp": request.headers.get("svix-timestamp"),
                "svix-signature": request.headers.get("svix-signature"),
            }

            wh = Webhook( CREATE_USER_WEBHOOK_SECRET if request.url.path == "/api/v1/create_user" else CREATE_ORGANIZATION_WEBHOOK_SECRET )
            try:
                wh.verify(payloadString, svixHeaders)
            except Exception as e:
                logger.error(f"Webhook authentication failed: {str(e)}")
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid webhook signature"},
                )

        response = await call_next(request)
        return response