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
from responses import get_transcription_response
import base64


class TestAudioTranscription(unittest.TestCase):
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

        with open("sample_audio.wav", "rb") as f:
            bytes = base64.b64encode(f.read()).decode('utf')
        upload_response = get_upload_response(get_standard_body(self.ts, self.cId, self.username, self.token),
                                              files=[{
                                                "path": "user/texts/sample.wav",
                                                "data": bytes,
                                                "overwrite": True,
                                                "preprocess": False
                                              }])

    def tearDown(self):
        delete_response = get_delete_account_response(get_standard_body(self.ts, self.cId, self.username, self.token))

    def test_valid_transcribe(self):
        valid_path = 'user/texts/sample.wav'
        response = get_transcription_response(get_standard_body(self.ts, self.cId, self.username, self.token), valid_path)
        self.assertTrue('err' in response)
        self.assertEqual(0, response['err']['code'])
        self.assertEqual(self.cId, response['cId'])
        self.assertTrue(verify_timestamp(self.ts, response['ts']))

        self.assertTrue('data' in response['p'])
        self.assertTrue(isinstance(response['p']['data'], str))
        transcript = response['p']['data']
        try: # Ensure text is base64 encoded
            self.assertTrue(base64.b64encode(base64.b64decode(transcript.encode('ascii'))).decode('ascii') == transcript)
        except Exception as e:
            self.fail(str(e))

    def test_time(self):
        start = time.time()
        self.test_valid_transcribe()
        elapsed = math.floor((time.time() - start) * 1000)  # time in ms
        threshold = 200
        self.assertLessEqual(elapsed, threshold,
                             f"The function took longer than %d milliseconds to execute" % threshold)

    def test_invalid_path(self):
        bad_path = 'user/texts/badpath.txt'
        response = get_transcription_response(get_standard_body(self.ts, self.cId, self.username, self.token), bad_path)
        self.assertTrue('err' in response)
        self.assertEqual(11, response['err']['code'])
        self.assertEqual("The specified file at %s does not exist." % bad_path, response['err']['msg'])
        self.assertTrue('data' not in response['p'])


if __name__ == '__main__':
    unittest.main()
