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
from responses import get_upload_response
from responses import get_questions_response
import base64


class TestGetQA(unittest.TestCase):
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

        with open("sample_text.txt", "r") as f:
            text = f.read()
        upload_response = get_upload_response(get_standard_body(self.ts, self.cId, self.username, self.token),
                                              files=[{
                                                "path": "user/texts/khan1.txt",
                                                "data": text,
                                                "overwrite": True,
                                                "preprocess": False
                                              }])

    def tearDown(self):
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username, self.token))

    def test_valid_question(self):
        valid_path = 'user/texts/khan1.txt'
        response = get_questions_response(get_standard_body(self.ts, self.cId, self.username, self.token), valid_path, "When did the Byzantine Empire end?")
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.assertEqual(self.cId, response['cId'])
        self.assertTrue(verify_timestamp(self.ts, response['ts']))

        self.assertTrue('score' in response['p'])
        self.assertTrue(isinstance(response['p']['score'], float))
        self.assertTrue(0 <= response['p']['score'] <= 1)

        self.assertTrue('start' in response['p'])
        self.assertTrue(isinstance(response['p']['start'], int))

        self.assertTrue('end' in response['p'])
        self.assertTrue(isinstance(response['p']['end'], int))

        self.assertTrue('extractive_answer' in response['p'])
        self.assertTrue('abstractive_answer' in response['p'])
        ex_ans = response['p']['extractive_answer']
        ab_ans = response['p']['abstractive_answer']
        try: # Ensure text is base64 encoded
            self.assertTrue(base64.b64encode(base64.b64decode(ex_ans.encode('ascii'))).decode('ascii') == ex_ans)
            self.assertTrue(base64.b64encode(base64.b64decode(ab_ans.encode('ascii'))).decode('ascii') == ab_ans)
        except Exception as e:
            self.fail(str(e))

    def test_time(self):
        start = time.time()
        self.test_valid_question()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)

    def test_invalid_path(self):
        bad_path = 'user/texts/badpath.txt'
        response = get_questions_response(get_standard_body(self.ts, self.cId, self.username, self.token), bad_path, "When did the Byzantine Empire end?")
        self.assertTrue('err' in response)
        self.assertEqual(11, response['err']['code'])
        self.assertEqual("The specified file at %s does not exist." % bad_path, response['err']['msg'])
        self.assertTrue('score' not in response['p'])
        self.assertTrue('start' not in response['p'])
        self.assertTrue('end' not in response['p'])
        self.assertTrue('extractive_answer' not in response['p'])
        self.assertTrue('abstractive_answer' not in response['p'])


if __name__ == '__main__':
    unittest.main()
