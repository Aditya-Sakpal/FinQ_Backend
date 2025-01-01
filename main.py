import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.constants import ALLOWED_ORIGINS
from app.routers import files_router, organizations_router, users_router
from app.middleware.clerk_middleware import ClerkAuthMiddleware
from app.middleware.svix_middleware import SvixWebhookAuthMiddleware

app = FastAPI(
    title="My FastAPI Application",
    description="A simple FastAPI application.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS, 
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"], 
)
app.add_middleware(ClerkAuthMiddleware)
app.add_middleware(SvixWebhookAuthMiddleware)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  
    ]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

app.include_router(users_router.router, prefix="/api/v1")
app.include_router(organizations_router.router, prefix="/api/v1")
app.include_router(files_router.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3003)