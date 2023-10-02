import cgi


class POSTBody:
    def __init__(self, data):
        self.data = data

    def get(self, key):
        value = self.data.get(key, [''])
        if type(value) == str:
            value = cgi.escape(value)
        return value

    def set(self, key, value):
        self.data[key] = value

    def __iter__(self):
        for key, value in self.data:
            yield key, value


class Request:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.http_host = environ.get('HTTP_HOST')
        self.http_user_agent = environ.get('HTTP_USER_AGENT')
        self.lang = environ.get('LANG')
        self.method = environ.get('REQUEST_METHOD')
        self.path = environ.get('PATH_INFO')
        self.host_address = environ.get('HOST_ADDRESS')
        self.gateway_interface = environ.get('GATEWAY_INTERFACE')
        self.server_port = environ.get('SERVER_PORT')
        self.remote_host = environ.get('REMOTE_HOST')
        self.content_type = environ.get('CONTENT_TYPE')
        self.content_length = environ.get('CONTENT_LENGTH')
        self.query_string = environ.get('QUERY_STRING')
        self.server_protocol = environ.get('SERVER_PROTOCOL')
        self.server_software = environ.get('SERVER_SOFTWARE')
        self.start_response = start_response

        self.parse_qs()

    def parse_qs(self):
        if self.method != 'POST':
            return
        self.post = POSTBody({})
        environ = self.environ
        field_storage = cgi.FieldStorage(
            fp=environ.get('wsgi.input'),
            environ=environ,
            keep_blank_values=True,
        )

        for item in field_storage.list:
            if not item.filename:
                self.post.set(item.key, item.value)
            else:
                self.post.set(item.key, item)


