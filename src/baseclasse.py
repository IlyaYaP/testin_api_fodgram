from src.errors import ErrorMessaages


class Response():
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, statuse_code):
        if isinstance(statuse_code, list):
            assert self.response_status in statuse_code, ErrorMessaages.WRONG_STATUS_CODE
        else:
            assert self.response_status == statuse_code, ErrorMessaages.WRONG_STATUS_CODE
