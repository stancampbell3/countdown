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
            'choices': {
                'player1': 'cab',
                'player2': 'bead'
            },
            'letters': letters
        }
        response = self.app.post('/lettersround/submit', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(3, data['scores']['player1'])
        self.assertEqual(4, data['scores']['player2'])

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

    def test_select_numbers(self):
        response = self.app.get('/numbersround/select?num_large=2&num_small=4')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['numbers']), 6)

    def test_get_target_number(self):
        response = self.app.get('/numbersround/target')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('target_number', data)

    def test_validate_rachelriley_solution(self):
        payload = {
            'target': 532,
            'selection': [25, 50, 75, 100, 3, 6],
            'solution': '100 * 5 + 25 + 7'
        }
        response = self.app.post('/rachelriley/validate', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['difference'], 0)

    def test_solve_rachelriley(self):
        payload = {
            'target': 532,
            'selection': [25, 50, 75, 100, 3, 6]
        }
        response = self.app.post('/rachelriley/solve', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('solution', data)

    def test_generate_conundrum(self):
        response = self.app.get('/conundrumround/generate')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['conundrum']), 9)
        self.assertEqual(len(data['solution']), 9)
        self.assertNotEqual(data['conundrum'], data['solution'])
        self.assertTrue(data['solution'].isalpha())
        self.assertTrue(data['conundrum'].isalpha())
        self.assertCountEqual(data['conundrum'], data['solution'])

    def test_validate_conundrum_solution(self):
        conundrum = 'sselrewop'
        solution = 'powerless'
        payload = {
            'conundrum': conundrum,
            'solution': solution
        }
        response = self.app.post('/conundrumround/validate', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['is_valid'])

    if __name__ == '__main__':
        unittest.main()