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


class TestCreateNewUser(unittest.TestCase):
    def setUp(self):
        self.ts = get_unix_time_millis()
        self.cId = str(uuid.uuid4())
        self.username = "DoeJ1970"

    def tearDown(self):
        # need to delete the account we created. Means we need to login to get access token first
        login_response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        if "p" in login_response:
            delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username,
                                                                            login_response['p']['token']))

    def test_valid_user(self):
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.assertEqual(self.cId, response['cId'], "The correlation IDs did not match. Expected %s. Got %s" %
                         (self.cId, response['cId']))
        self.assertTrue(verify_timestamp(self.ts, response['ts']))
        self.assertEqual(self.username, response['p']['username'])

    def test_time(self):
        start = time.time()
        self.test_valid_user()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)

    def test_user_already_exists(self):
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)  # create valid user
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)  # try to create again
        self.assertTrue('err' in response)
        self.assertEqual(15, response['err']['code'])

    # def test_invalid_email(self):
    #     # test empty email
    #     response = get_new_user_response(self.ts, self.cId, email="", password="QwertY123!",
    #                                      birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
    #                                      phone=12345678901, job=0, username=self.username)
    #     self.assertTrue('err' in response)
    #     self.assertEqual(3, response['err']['code'])
    #     # test missing email field
    #     response = get_new_user_response(self.ts, self.cId, email="", password="QwertY123!",
    #                                      birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
    #                                      phone=12345678901, job=0, username=self.username,
    #                                      remove_payload_keys=['email'])
    #     self.assertTrue('err' in response)
    #     self.assertEqual(1, response['err']['code'])
    #     # test malformed text input
    #     response = get_new_user_response(self.ts, self.cId, email="thisiswrong", password="QwertY123!",
    #                                      birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
    #                                      phone=12345678901, job=0, username=self.username)
    #     self.assertTrue('err' in response)
    #     self.assertEqual(3, response['err']['code'])
    #     # test null bytes in text input
    #     response = get_new_user_response(self.ts, self.cId, email="\x00", password="QwertY123!",
    #                                      birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
    #                                      phone=12345678901, job=0, username=self.username)
    #     self.assertTrue('err' in response)
    #     self.assertEqual(3, response['err']['code'])
    #     # test malformed type
    #     response = get_new_user_response(self.ts, self.cId, email=0, password="QwertY123!",
    #                                      birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
    #                                      phone=12345678901, job=0, username=self.username)
    #     self.assertTrue('err' in response)
    #     self.assertEqual(2, response['err']['code'])
    #
    # def test_invalid_password(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_birthday(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_org(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_firstname(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_lastname(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_gender(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_phone(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_job(self):
    #     raise NotImplementedError("error")
    #
    # def test_invalid_username(self):
    #     raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
