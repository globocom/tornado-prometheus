# Tornado prometheus
![build](https://travis-ci.org/globocom/tornado-prometheus.svg?branch=master)

HTTP metrics for a tornado application

# Installing


# Usage

```python
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
```
