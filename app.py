from flask import Flask, render_template, request
from core.letters_round import LettersRound

app = Flask(__name__)
letters_round = LettersRound()

@app.route('/')
def index():
    letters = letters_round.select_letters(3, 6)
    return render_template('index.html', letters=letters)

@app.route('/submit', methods=['POST'])
def submit():
    team1_word = request.form['team1_word']
    letters_round.submit_words(team1_word, '')
    letters = letters_round.letters
    return render_template('index.html', letters=letters, team1_word=team1_word, team2_word='')

if __name__ == '__main__':
    app.run(debug=True)