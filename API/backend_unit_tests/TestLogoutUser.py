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

class TestLogoutUser(unittest.TestCase):
    def setUp(self):
        self.ts = get_unix_time_millis()
        self.cId = str(uuid.uuid4())
        self.username = "DoeJ1970"
        self.token = ""
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)  # create user to test login

    def tearDown(self):
        # need to delete the account we created. Means we need to login to get access token first
        login_response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        if 'token' not in login_response['p']:
            print(json.dumps(login_response))
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username,
                                                                        login_response['p']['token']))

    def test_valid_logout_one_session(self):
        # Default maximum connections on the account should be 2.
        # Test logging out the first account when it is only one logged in
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        response = get_logout_user_response(self.ts, self.cId, self.username, response['p']['token'], logout_all=False)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])

    def test_valid_logout_two_sessions(self):
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                           ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                           browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                           location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token1 = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token2 = response['p']['token']
        response = get_logout_user_response(self.ts, self.cId, self.username, token1, logout_all=False)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])
        response = get_logout_user_response(self.ts, self.cId, self.username, token2, logout_all=False)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])

    def test_valid_logout_two_sessions_reversed(self):
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                           ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                           browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                           location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token1 = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token2 = response['p']['token']
        response = get_logout_user_response(self.ts, self.cId, self.username, token2, logout_all=False)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])
        response = get_logout_user_response(self.ts, self.cId, self.username, token1, logout_all=False)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])

    def test_time(self):
        start = time.time()
        self.test_valid_logout_two_sessions_reversed()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)

    def test_valid_logout_all_single(self):
        # Default maximum connections on the account should be 2.
        # Test logging out all accounts when there is one session active
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        response = get_logout_user_response(self.ts, self.cId, self.username, response['p']['token'], logout_all=True)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(1, response['p']['count'])

    def test_valid_logout_all_double_first_token(self):
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                           ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                           browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                           location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token1 = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token2 = response['p']['token']
        response = get_logout_user_response(self.ts, self.cId, self.username, token1, logout_all=True)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(2, response['p']['count'])

    def test_valid_logout_all_double_second_token(self):
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                           ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                           browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                           location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token1 = response['p']['token']
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token2 = response['p']['token']
        response = get_logout_user_response(self.ts, self.cId, self.username, token2, logout_all=True)
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])
        self.assertEqual(2, response['p']['count'])

    def test_logout_invalid_token(self):
        # test where username logged in but token doesn't match
        response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                           ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                           browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                           location="Milwaukee WI", redirect="example.com/index")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        token1 = response['p']['token']
        response = get_logout_user_response(self.ts, self.cId, username=self.username,
                                            token=str(uuid.uuid4()), logout_all=True)
        self.assertTrue('err' in response)
        self.assertEqual(23, response['err']['code'])
        response = get_logout_user_response(self.ts, self.cId, username=self.username,
                                            token=str(uuid.uuid4()), logout_all=False)
        self.assertTrue('err' in response)
        self.assertEqual(23, response['err']['code'])
        # test where username not logged in (no sessions). Nothing for token to match
        response = get_logout_user_response(self.ts, self.cId, username="ThisUsernameDontExist",
                                            token=str(uuid.uuid4()), logout_all=True)
        self.assertTrue('err' in response)
        self.assertEqual(22, response['err']['code'])
        response = get_logout_user_response(self.ts, self.cId, username="ThisUsernameDontExist",
                                            token=str(uuid.uuid4()), logout_all=False)
        self.assertTrue('err' in response)
        self.assertEqual(22, response['err']['code'])
        # test where different username has the token we send.
        response = get_logout_user_response(self.ts, self.cId, username="ThisUsernameDontExist",
                                            token=token1, logout_all=True)
        self.assertTrue('err' in response)
        self.assertEqual(22, response['err']['code'])
        response = get_logout_user_response(self.ts, self.cId, username="ThisUsernameDontExist",
                                            token=token1, logout_all=False)
        self.assertTrue('err' in response)
        self.assertEqual(22, response['err']['code'])
        # cleanup by logging out
        response = get_logout_user_response(self.ts, self.cId, username=self.username,
                                            token=token1, logout_all=False)

    def test_logout_account_doesnt_exist(self):
        response = get_logout_user_response(self.ts, self.cId, username="ThisUsernameDontExist",
                                            token=str(uuid.uuid4()), logout_all=True)
        self.assertTrue('err' in response)
        self.assertEqual(22, response['err']['code'])

    # def test_invalid_username(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_token(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_logout_specifier(self):
    #     # refers to the all keyword
    #     raise NotImplementedError("error")
    #
    # def test_invalid_payload(self):
    #     raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
