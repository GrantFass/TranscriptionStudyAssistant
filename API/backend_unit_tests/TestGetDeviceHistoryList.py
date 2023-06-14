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
from responses import get_device_history_list_response
import sys


class TestGetDeviceHistoryList(unittest.TestCase):
    def setUp(self):
        self.ts = get_unix_time_millis()
        self.cId = str(uuid.uuid4())
        self.username = "DoeJ1970"
        response = get_new_user_response(self.ts, self.cId, email="example@mail.net", password="QwertY123!",
                                         birthday="12/25/1970", org="MSOE", first="Jane", last="Doe", gender=3,
                                         phone=12345678901, job=0, username=self.username)  # create user to test login
        # login the created user
        login_response = get_login_user_response(self.ts, self.cId, self.username, password="QwertY123!",
                                                 ip="75.103.1.21", os="Microsoft Windows (build 103)",
                                                 browser="Mozilla Firefox (build 1.1.2)", device="Unknown",
                                                 location="Milwaukee WI", redirect="example.com/index")
        self.token = login_response['p']['token']

    def tearDown(self):
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username, self.token))

    def standard_valid_test_asserts(self, response):
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.assertEqual(self.cId, response['cId'])
        self.assertTrue(verify_timestamp(self.ts, response['ts']))

    def valid_test_asserts(self, response):
        self.assertTrue('list' in response['p'])
        self.assertEqual(1, len(response['p']['list']))
        self.assertEqual('Mozilla Firefox (build 1.1.2)', response['p']['list'][0]['browser'])
        self.assertEqual('Unknown', response['p']['list'][0]['device'])
        self.assertEqual('75.103.1.21', response['p']['list'][0]['ip'])
        self.assertEqual('Milwaukee WI', response['p']['list'][0]['location'])
        self.assertEqual('Microsoft Windows (build 103)', response['p']['list'][0]['os'])
        self.assertTrue(response['p']['list'][0]['ts'] < get_unix_time_millis())

    def test_history_one_entry(self):
        response = get_device_history_list_response(get_standard_body(self.ts, self.cId, self.username, self.token,
                                                                      remove_standard_keys=None),
                                                    num=1, remove_payload_keys=None)
        self.standard_valid_test_asserts(response)
        self.valid_test_asserts(response)

    def test_history_all_entry(self):
        response = get_device_history_list_response(get_standard_body(self.ts, self.cId, self.username, self.token,
                                                                      remove_standard_keys=None),
                                                    num=-1, remove_payload_keys=None)
        self.standard_valid_test_asserts(response)
        self.valid_test_asserts(response)

    def test_history_zero_entry(self):
        response = get_device_history_list_response(get_standard_body(self.ts, self.cId, self.username, self.token,
                                                                      remove_standard_keys=None),
                                                    num=0, remove_payload_keys=None)
        self.standard_valid_test_asserts(response)
        self.assertTrue('list' in response['p'])
        self.assertEqual(0, len(response['p']['list']))

    def test_history_max_int_entry(self):
        response = get_device_history_list_response(get_standard_body(self.ts, self.cId, self.username, self.token,
                                                                      remove_standard_keys=None),
                                                    num=sys.maxsize, remove_payload_keys=None)
        self.standard_valid_test_asserts(response)
        self.valid_test_asserts(response)

    # def test_invalid_num(self):
    #     raise NotImplementedError("error")

    def test_time(self):
        start = time.time()
        self.test_history_max_int_entry()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)


if __name__ == '__main__':
    unittest.main()
