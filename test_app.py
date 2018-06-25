#boeing test

import unittest
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/dev')
        self.assertEqual(response.text, 'Hello World!')

class TestFlaskApiUsingPostRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.post('https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/dev', data = "SampleName")
        self.assertEqual(response.text, 'Hello SampleName World!')


if __name__ == "__main__":
    unittest.main()
