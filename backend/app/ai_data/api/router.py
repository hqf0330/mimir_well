from fastapi import APIRouter

from backend.app.ai_data.api.v1.conn_source import router as conn_router

from backend.core.conf import settings

# Keep child router with full prefix to avoid empty-prefix collisions
v1 = APIRouter(tags=['数据源'])
v1.include_router(conn_router, prefix=f"{settings.FASTAPI_API_V1_PATH}/conn")

