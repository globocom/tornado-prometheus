from tornado.web import RequestHandler
from prometheus_client import Histogram, Counter, REGISTRY
from prometheus_client.exposition import choose_encoder

BUCKETS = (0.01, 0.05, 0.1, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0)


class PrometheusMixIn(object):
    def __init__(self, *args, **kwargs):
        super(PrometheusMixIn, self).__init__(*args, **kwargs)

        self.request_time_seconds = Histogram(
            namespace="tornado",
            subsystem="http",
            name="request_duration_seconds",
            documentation="HTTP request duration in seconds",
            buckets=BUCKETS,
            labelnames=("handler", "method"),
        )

        self.requests_total = Counter(
            namespace="tornado",
            subsystem="http",
            name="requests_total",
            documentation="Total of HTTP requests processed",
            labelnames=("handler", "method", "status"),
        )

    def observe_request(self, handler):
        handler_name = type(handler).__name__
        method = handler.request.method
        request_time = handler.request.request_time()
        status = handler.get_status()

        self.request_time_seconds.labels(handler_name, method).observe(request_time)
        self.requests_total.labels(
            handler_name, method, classify_status_code(status)
        ).inc()

    def log_request(self, handler):
        super(PrometheusMixIn, self).log_request(handler)
        self.observe_request(handler)


def classify_status_code(status_code):
    """
    Prometheus recomends to have lower number of cardinality,
    each combination creates a new metric in datastore,
    to reduce this risk we store only the class of status code
    """
    if 200 <= status_code < 300:
        return "2xx"

    if 300 <= status_code < 400:
        return "3xx"

    if 400 <= status_code < 500:
        return "4xx"

    return "5xx"


class MetricsHandler(RequestHandler):
    def get(self):
        encoder, content_type = choose_encoder(self.request.headers.get('accept'))
        self.set_header("Content-Type", content_type)
        self.write(encoder(REGISTRY))
