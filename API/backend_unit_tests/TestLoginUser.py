import json
import math
import time
import unittest
import uuid
from responses import get_unix_time_millis
from responses import get_login_user_response
from responses import get_delete_account_response
from responses import get_standard_body
from responses import get_new_user_response
from responses import verify_timestamp
from responses import get_logout_user_response


class TestLoginUser(unittest.TestCase):
    def setUp(self):
        self.ts = get_unix_time_millis()
        self.cId = str(uuid.uuid4())
        self.username = "DoeJ1970"
        self.token = ""
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)  # create user to test login

    def tearDown(self):
        # need to logout any remaining sessions for the active user
        if self.token:
            logout_response = get_logout_user_response(self.ts, self.cId, self.username, self.token, logout_all=True)
        # need to delete the account we created. Means we need to login to get access token first
        login_response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        if 'token' not in login_response['p']:
            print(json.dumps(login_response))
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username,
                                                                        login_response['p']['token']))

    def test_valid_request(self):
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.token = response['p']['token']
        self.assertEqual(uuid.UUID(self.token).version, 4, "The returned token was not a version4 UUID.")

    def test_time(self):
        start = time.time()
        self.test_valid_request()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)

    def test_too_many_connections(self):
        # Default maximum connections on the account should be 2. Therefore third login should fail.
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.token = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.token = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(25, response['err']['code'])

    def test_account_not_found(self):
        response = get_login_user_response(self.ts, self.cId, username="ThisUsernameDontExist", password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(10, response['err']['code'])

    # def test_invalid_username(self):
    #     # should be the same for every endpoint due to being processed under the receive method.
    #     raise NotImplementedError("error")
    #
    # def test_invalid_password(self):
    #     # password does not match + malformed passwords
    #     raise NotImplementedError("error")
    #
    # def test_invalid_ip(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_os(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_browser(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_device(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_location(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_redirect(self):
    #     raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
