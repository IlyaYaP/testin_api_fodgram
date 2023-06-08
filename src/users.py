from src.base_validate import Response


class UsersValidate(Response):

    def user_assert_bad_request(self, statuse_code):
        self.assert_status_code(400)

        
