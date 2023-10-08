from app import App
from request import Request
from response import HttpResponse, JsonResponse
from router import Path
from wsgiref.simple_server import make_server

app = App()

def hello_world(request: Request):
    return HttpResponse(request, 'Hello World')

def json_world(request: Request):
    return JsonResponse(request, {"hello": "world"})


routes = [
    Path('/', hello_world),
    Path('/json', json_world),
]
app.set_routes(routes)
server = make_server("127.0.0.1", 8000, app)
server.serve_forever()
