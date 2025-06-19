from http import HTTPStatus
from fastapi import FastAPI, Response
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)

import random
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    'http_request_total',
    'Total HTTP Request',
    ['method', 'time', 'endpoint', 'status']
)



@app.get("/random")
def get_random_number():
    endpoint_name = '/random'
    method_name = 'GET'
    start_time = time.time()

    number = random.randint(1, 1000)

    REQUEST_COUNT.labels(
        method=method_name,
        time=time.time(),
        endpoint=endpoint_name,
        status=HTTPStatus.OK
    ).inc()

    latency = time.time() - start_time

    return {
        "number" : number,
        "latency" : latency
    }

@app.get("/metrics")
def get_metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )