import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from metrics import REQUEST_COUNT, REQUEST_LATENCY

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        endpoint = request.url.path
        start_time = time.time()

        response = await call_next(request)

        latency = time.time() - start_time
        status = response.status_code

        REQUEST_LATENCY.labels(
            method=method,
            endpoint=endpoint
        ).observe(latency)

        REQUEST_COUNT.labels(
            method=method,
            endpoint=endpoint,
            status=status
        ).inc()


        return response
    
