import unittest
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://127.0.0.1:5000')
        self.assertEqual(response.text, 'Hello World!')

class TestFlaskApiUsingPostRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.post('http://127.0.0.1:5000', data = "SampleName")
        self.assertEqual(response.text, 'Hello SampleName World!')


if __name__ == "__main__":
    unittest.main()