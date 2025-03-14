from flask import Flask, jsonify, request
from core.letters_round import LettersRound
from core.susie_dent import SusieDent
from core.numbers_round import NumbersRound
from core.rachel_riley import RachelRiley, validate_solution

app = Flask(__name__)
letters_round = LettersRound()
susie_dent = SusieDent()
numbers_round = NumbersRound()
rachel_riley = RachelRiley()


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
    team1_word = data.get('team1_word')
    team2_word = data.get('team2_word')
    letters = data.get('letters')
    team1_score, team2_score = letters_round.score_round(team1_word, team2_word, letters)
    return jsonify({'team1_score': team1_score, 'team2_score': team2_score})


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
    difference = validate_solution(target, selection, solution)
    return jsonify({'difference': difference})


@app.route('/rachelriley/solve', methods=['POST'])
def solve_rachelriley():
    data = request.get_json()
    target = data.get('target')
    selection = data.get('selection')
    solution = rachel_riley.find_solution(target, selection)
    return jsonify({'solution': solution})


if __name__ == '__main__':
    app.run(debug=True)
