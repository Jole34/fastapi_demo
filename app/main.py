from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.api import api_router
from config.setup import settings


app = FastAPI(
    title="Test", openapi_url="/api/openapi.json", redoc_url="/documentation",

)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api")
