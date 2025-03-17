# Countdown Game Show

This is a toy implementation of the Countdown game show in Python using Flask to deliver a REST API.

## Features

- Simulates the letters round of the Countdown game show.
- Simulates the numbers round of the Countdown game show.
- Allows selection of letters from vowel and consonant pools that reflect their frequency in the English language.
- Provides scoring for words based on their length and validity.
- Includes a REST API for interacting with the game.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/stancampbell3/countdown.git
    cd countdown
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the NLTK WordNet data:
    ```python
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Letters Round
- `GET /lettersround/select`: Selects a set of letters for the game.
    ```sh
    curl -X GET "http://127.0.0.1:5000/lettersround/select?num_vowels=3&num_consonants=6"
    ```

- `POST /lettersround/submit`: Submits words for scoring.
    ```sh
    curl -X POST http://127.0.0.1:5000/lettersround/submit -H "Content-Type: application/json" -d '{"team1_word": "mouse", "team2_word": "cat", "letters": ["M", "O", "U", "S", "E", "C", "A", "T"]}'
    ```

### Susie Dent
- `POST /susiedent/validate`: Validates if a word is an English word.
    ```sh
    curl -X POST http://127.0.0.1:5000/susiedent/validate -H "Content-Type: application/json" -d '{"word": "mouse"}'
    ```

- `POST /susiedent/better`: Finds better words from the given letters.
    ```sh
    curl -X POST http://127.0.0.1:5000/susiedent/better -H "Content-Type: application/json" -d '{"letters": ["M", "O", "U", "S", "E", "C", "A", "T"], "target_words": ["cat", "mouse"]}'
    ```

### Numbers Round
- `GET /numbersround/select`: Selects a set of numbers for the game.
    ```sh
    curl -X GET "http://127.0.0.1:5000/numbersround/select?num_large=2&num_small=4"
    ```

- `GET /numbersround/target`: Gets the target number for the numbers round.
    ```sh
    curl -X GET http://127.0.0.1:5000/numbersround/target
    ```

### Rachel Riley
- `POST /rachelriley/validate`: Validates a solution for the numbers round.
    ```sh
    curl -X POST http://127.0.0.1:5000/rachelriley/validate -H "Content-Type: application/json" -d '{"target": 532, "selection": [25, 50, 75, 100, 3, 6], "solution": "100 * 5 + 25 + 7"}'
    ```

- `POST /rachelriley/solve`: Finds a solution for the numbers round.
    ```sh
    curl -X POST http://127.0.0.1:5000/rachelriley/solve -H "Content-Type: application/json" -d '{"target": 532, "selection": [25, 50, 75, 100, 3, 6]}'
    ```

## Running Tests

To run the tests, use the following command:
```sh
python -m unittest discover tests