import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your word:', response.data)

    def test_submit_page(self):
        response = self.app.post('/submit', data=dict(team1_word='example'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Other team\'s guess:', response.data)
        # self.assertIn(b'example', response.data)

if __name__ == '__main__':
    unittest.main()