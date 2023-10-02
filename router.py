class Path:
    def __init__(self, path, func):
        self.path = path
        self.func = func

    def isMatch(self, path):
        if self.path == path:
            return True
        else:
            return False


class Router:
    def __init__(self, routes=None):
        self.routes = list(routes) if routes else []
