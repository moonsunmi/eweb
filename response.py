from typing import Callable
import json


class Response:
    def __init__(self, request, status_code, content_type):
        self.headers: list = [('Content-type', content_type)]
        self.start_response: Callable = request.start_response
        self.status_code: str = status_code
        self.content_type: str = content_type
        self.response_content: list = []

    def make_response(self):
        self.start_response(self.status_code, self.headers)
        return self.response_content


class HttpResponse(Response):
    def __init__(self, request, content, status_code, content_type='text/html'):
        super().__init__(request, status_code, content_type)
        if type(content) == str:
            content = content.encode()
        self.response_content.append(content)


class JsonResponse(Response):
    def __init__(self, request, content, status_code, content_type='application/json'):
        super().__init__(request, status_code, content_type)
        content = json.dumps(content)
        self.response_content.append(content)


class ErrorResponse(Response):
    def __init__(self, request, error_code: str):
        super().__init__(request, status_code=error_code, content_type='text/html')


class Http404(ErrorResponse):
    def __init__(self, request, error_code='404 Not Found'):
        super().__init__(request, error_code)
        self.response_content.append('404 Not Found'.encode())
