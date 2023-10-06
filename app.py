from request import Request
from router import Router
from response import Response, Http404


class App:
    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        print(f'environ: f{environ}')
        request = Request(environ, start_response)
        try:
            print(f'Incoming request: f{request.path}')
            func = self.router.get_route(request.path)
            if func is not None:
                response = func(request)
                return response.make_response()
            return Http404(request).make_response()
        except Exception as e:
            print(e)
            return Http404(request).make_response()