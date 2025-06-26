from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_total',
    'HTTP request latency',
    ['method', 'endpoint']
)

DATABASE_OPERATIONS = Counter(
    'database_operations_total',
    'Total Database Operations',
    ['operation', 'table']
)

ACTIVE_USERS = Gauge(
    'active_users',
    'Current number of active users'
)