import unittest
import uuid
from responses import get_unix_time_millis
from responses import get_login_user_response
from responses import get_delete_account_response
from responses import get_standard_body
from responses import get_new_user_response
from responses import verify_timestamp
from responses import get_logout_user_response


class TestStandardMessageComponents(unittest.TestCase):
    """
    The standard message components should be able to be tested with most endpoints.
    This is because they are processed under the receive method in the backend.
    The username and token components should be tested to see what occurs when sent to auth vs other endpoints.
    There is a standard payload message component test as well.
    An error should be returned for the payload test when it is empty or exists when it should not.
    Specific payload fields for various endpoints are tested under their associated test classes.
    """
    def setUp(self):
        pass
        # self.ts = get_unix_time_millis()
        # self.cId = str(uuid.uuid4())
        # self.username = "DoeJ1970"
        # response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
        #                                  birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
        #                                  phone=12345678901, job=0, username=self.username)  # create user to test login

    def tearDown(self):
        pass
        # # need to delete the account we created. Means we need to login to get access token first
        # login_response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
        #                                          ip="75.103.1.21", os="Microsoft Windows (build 103)",
        #                                          browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
        #                                          location="Milwaukee WI", redirect="example.com/index")
        # if 'token' not in login_response['p']:
        #     print(json.dumps(login_response))
        # delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username,
        #                                                                 login_response['p']['token']))

    def test_invalid_timestamp(self):
        raise NotImplementedError("error")

    def test_invalid_cId(self):
        raise NotImplementedError("error")

    def test_invalid_username(self):
        # test for auth endpoint
        # test for other endpoint
        raise NotImplementedError("error")

    def test_invalid_token(self):
        raise NotImplementedError("error")

    def test_invalid_payload(self):
        raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
