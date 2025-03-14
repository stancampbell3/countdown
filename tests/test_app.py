import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_select_letters_valid(self):
        response = self.app.get('/lettersround/select?num_vowels=3&num_consonants=6')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['letters']), 9)

    def test_select_letters_invalid(self):
        response = self.app.get('/lettersround/select?num_vowels=2&num_consonants=7')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_submit_words(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        payload = {
            'team1_word': 'abc',
            'team2_word': 'def',
            'letters': letters
        }
        response = self.app.post('/lettersround/submit', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('team1_score', data)
        self.assertIn('team2_score', data)

    def test_validate_word(self):
        payload = {'word': 'mouse'}
        response = self.app.post('/susiedent/validate', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['is_valid'])

    def test_find_better_words(self):
        payload = {
            'letters': ['m', 'o', 'u', 's', 'e', 'c', 'a', 't'],
            'target_words': ['mouse', 'cat']
        }
        response = self.app.post('/susiedent/better', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('better_words', data)

if __name__ == '__main__':
    unittest.main()