Tornado prometheus
==================

.. image:: https://travis-ci.org/globocom/tornado-prometheus.svg?branch=master
    :target: https://travis-ci.org/globocom/tornado-prometheus

HTTP metrics for a tornado application

Installing
----------

.. code-block:: bash

   pip install tornado-prometheus


Usage
-----

.. code-block:: python

    from tornado.web import Application, RequestHandler
    from tornado.ioloop import IOLoop

    from tornado_prometheus import PrometheusMixIn, MetricsHandler

    class SampleApp(PrometheusMixIn, Application):
        pass

    if __name__ == '__main__':
      app =  SampleApp([
          (r"/metrics", MetricsHandler),
      ])

      app.listen(8888)
      IOLoop.current().start()


Example output for metric route
-------------------------------

.. code-block::

   # HELP tornado_http_request_duration_seconds HTTP request duration in seconds
   # TYPE tornado_http_request_duration_seconds histogram
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="0.01",method="GET"} 0.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="0.05",method="GET"} 0.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="0.1",method="GET"} 1.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="0.5",method="GET"} 1.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="0.75",method="GET"} 1.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="1.0",method="GET"} 1.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="2.5",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="5.0",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="7.5",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="10.0",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="15.0",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="20.0",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="30.0",method="GET"} 2.0
   tornado_http_request_duration_seconds_bucket{handler="StatusHandler",le="+Inf",method="GET"} 2.0

   # HELP tornado_http_requests_total Total of HTTP requests processed
   # TYPE tornado_http_requests_total counter
   tornado_http_requests_total{handler="StatusHandler",method="GET",status="2xx"} 2.0
