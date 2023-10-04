from request import Request
from typing import Callable


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
