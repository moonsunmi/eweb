from request import Request
from router import Router
from response import Response


class App:
    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        try:
            request = Request(environ, start_response)
            func = self.router.get_route(request.path)
            if func is not None:
                response = func(request)

        except:
            pass