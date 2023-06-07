from src.base_validate import Response


class UsersValidate(Response):

    def user_assert_bad_assert(self, statuse_code):
        if isinstance(statuse_code, list):
            assert self.response_status in statuse_code, ErrorMessaages.WRONG_STATUS_CODE
        else:
            assert self.response_status == statuse_code, ErrorMessaages.WRONG_STATUS_CODE
        
