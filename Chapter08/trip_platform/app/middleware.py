import logging

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

logger = logging.getLogger("uvicorn.error")

class ClientInfoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        host_client = request.client.host
        requested_path = request.url.path
        method = request.method

        logger.info(
            f"host client {host_client} requeted {method} {requested_path} endpoint"
        )

        return await call_next(request)