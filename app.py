from flask import Flask, jsonify, request
from core.letters_round import LettersRound
from core.susie_dent import SusieDent
from core.numbers_round import NumbersRound
from core.rachel_riley import RachelRiley
from core.conundrum_round import ConundrumRound

app = Flask(__name__)
letters_round = LettersRound()
susie_dent = SusieDent()
numbers_round = NumbersRound()
rachel_riley = RachelRiley()
conundrum_round = ConundrumRound()

@app.route('/lettersround/select', methods=['GET'])
def select_letters():
    num_vowels = int(request.args.get('num_vowels'))
    num_consonants = int(request.args.get('num_consonants'))
    try:
        letters = letters_round.select_letters(num_vowels, num_consonants)
        return jsonify({'letters': letters})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/lettersround/submit', methods=['POST'])
def submit_words():
    data = request.get_json()
    choices = data.get('choices')
    letters = data.get('letters')
    scores = letters_round.score_round(choices, letters)
    return jsonify({'scores': scores})

@app.route('/susiedent/validate', methods=['POST'])
def validate_word():
    data = request.get_json()
    word = data.get('word')
    is_valid = susie_dent.is_valid_english_word(word)
    return jsonify({'word': word, 'is_valid': is_valid})

@app.route('/susiedent/better', methods=['POST'])
def find_better_words():
    data = request.get_json()
    letters = data.get('letters')
    target_words = data.get('target_words')
    better_words = susie_dent.could_we_have_done_any_better(letters, target_words)
    return jsonify({'better_words': better_words})

@app.route('/numbersround/select', methods=['GET'])
def select_numbers():
    num_large = int(request.args.get('num_large'))
    num_small = int(request.args.get('num_small'))
    try:
        numbers = numbers_round.get_number_selections(num_large, num_small)
        return jsonify({'numbers': numbers})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/numbersround/target', methods=['GET'])
def get_target_number():
    target_number = numbers_round.find_target_number()
    return jsonify({'target_number': target_number})

@app.route('/rachelriley/validate', methods=['POST'])
def validate_rachelriley_solution():
    data = request.get_json()
    target = data.get('target')
    selection = data.get('selection')
    solution = data.get('solution')
    difference = rachel_riley.validate_solution(target, selection, solution)
    return jsonify({'difference': difference})

@app.route('/rachelriley/solve', methods=['POST'])
def solve_rachelriley():
    data = request.get_json()
    target = data.get('target')
    selection = data.get('selection')
    solution = rachel_riley.find_solution(target, selection)
    return jsonify({'solution': solution})

@app.route('/rachelriley/solvefromquery', methods=['GET'])
def solve_rachelriley_from_query():
    try:
        target = int(request.args.get('target'))
        selection = list(map(int, request.args.get('selection').split(',')))
        solution = rachel_riley.find_solution(target, selection)
        return jsonify({'target': target, 'selection': selection, 'solution': solution})
    except (ValueError, TypeError) as e:
        return jsonify({'error': 'Invalid input. Ensure target is an integer and selection is a comma-separated list of numbers.'}), 400

@app.route('/conundrumround/generate', methods=['GET'])
def generate_conundrum():
    conundrum, solution = conundrum_round.generate_conundrum()
    return jsonify({'conundrum': conundrum, 'solution': solution})

@app.route('/conundrumround/validate', methods=['POST'])
def validate_conundrum_solution():
    data = request.get_json()
    conundrum = data.get('conundrum')
    solution = data.get('solution')
    is_valid = conundrum_round.validate_solution(conundrum, solution)
    return jsonify({'conundrum': conundrum, 'solution': solution, 'is_valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)