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
- `GET /letters`: Selects a set of letters for the game.
    ```sh
    curl -X GET http://127.0.0.1:5000/letters
    ```

- `POST /score`: Submits words for scoring.
    ```sh
    curl -X POST http://127.0.0.1:5000/score -H "Content-Type: application/json" -d '{"team1_word": "mouse", "team2_word": "cat"}'
    ```

- `GET /longest_word`: Finds the longest possible word from the given letters.
    ```sh
    curl -X GET http://127.0.0.1:5000/longest_word?letters=mousecat
    ```

### Numbers Round
- `GET /numbers`: Selects a set of numbers for the game.
    ```sh
    curl -X GET http://127.0.0.1:5000/numbers
    ```

- `POST /solve`: Submits a solution for the numbers round.
    ```sh
    curl -X POST http://127.0.0.1:5000/solve -H "Content-Type: application/json" -d '{"numbers": [100, 75, 50, 25, 6, 3], "target": 952}'
    ```

## Running Tests

To run the tests, use the following command:
```sh
python -m unittest discover tests