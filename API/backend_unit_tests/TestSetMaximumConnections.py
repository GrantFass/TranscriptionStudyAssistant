import json
import math
import time
import unittest
import uuid

import responses
from responses import get_unix_time_millis
from responses import get_login_user_response
from responses import get_delete_account_response
from responses import get_standard_body
from responses import get_new_user_response
from responses import verify_timestamp
from responses import get_logout_user_response


class TestSetMaximumConnections(unittest.TestCase):
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
        if 'token' not in login_response['p']:
            print(json.dumps(login_response))
        self.token = login_response['p']['token']

    def tearDown(self):
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username, self.token))

    def test_set_max(self):
        max_conns = 8
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          max_conns, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], max_conns)

    def test_set_default(self):
        max_conns = 2
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          max_conns, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], max_conns)

    def test_set_minimum(self):
        max_conns = 1
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          max_conns, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], max_conns)

    def test_set_invalid(self):
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          0, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], 2)
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          -1, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], 2)
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          9, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], 2)
        connections_response = responses.set_maximum_connections_response(get_standard_body(self.ts,
                                                                                            self.cId,
                                                                                            self.username,
                                                                                            self.token),
                                                                          200, remove_payload_keys=None)
        self.assertEqual(connections_response['p']['max'], 2)

    def test_time(self):
        start = time.time()
        self.test_set_max()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)


if __name__ == '__main__':
    unittest.main()
