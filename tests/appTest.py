
import unittest
from app.app import app

class AppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_print_health_check(self):
        response = self.client.get('/health-check')
        self.assertEqual(response.status_code, 200)

    def test_print_hello_success(self):
        response = self.client.get('/hello?name=Maria')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, Maria!')

    def test_print_hello_error(self):
        response = self.client.get('/hello')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode('utf-8'), 'Nome não informado')


if __name__ == "__main__":
    unittest.main()