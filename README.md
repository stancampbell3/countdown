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

- **`GET /lettersround/select`**
    - **Description**: Selects letters for the letters round.
    - **Parameters**:
        - `num_vowels` (int): Number of vowels to select.
        - `num_consonants` (int): Number of consonants to select.
    - **Response**:
        - `200 OK`: Returns the selected letters.
        - `400 Bad Request`: Returns an error message if the parameters are invalid.

- **`POST /lettersround/submit`**
    - **Description**: Submits words for scoring in the letters round.
    - **Request Body**:
        - `choices` (dict): A map of player IDs to their chosen words.
        - `letters` (list): The list of selected letters.
    - **Response**:
        - `200 OK`: Returns the scores for each player.

### Susie Dent

- **`POST /susiedent/validate`**
    - **Description**: Validates if a word is an English word.
    - **Request Body**:
        - `word` (str): The word to validate.
    - **Response**:
        - `200 OK`: Returns whether the word is valid.

- **`POST /susiedent/better`**
    - **Description**: Finds better words from the given letters.
    - **Request Body**:
        - `letters` (list): The list of letters.
        - `target_words` (list): The list of target words.
    - **Response**:
        - `200 OK`: Returns a list of better words.

### Numbers Round

- **`GET /numbersround/select`**
    - **Description**: Selects numbers for the numbers round.
    - **Parameters**:
        - `num_large` (int): Number of large numbers to select.
        - `num_small` (int): Number of small numbers to select.
    - **Response**:
        - `200 OK`: Returns the selected numbers.
        - `400 Bad Request`: Returns an error message if the parameters are invalid.

- **`GET /numbersround/target`**
    - **Description**: Generates a target number for the numbers round.
    - **Response**:
        - `200 OK`: Returns the target number.

### Rachel Riley

- **`POST /rachelriley/validate`**
    - **Description**: Validates a solution for the numbers round.
    - **Request Body**:
        - `target` (int): The target number.
        - `selection` (list): The list of selected numbers.
        - `solution` (str): The solution to validate.
    - **Response**:
        - `200 OK`: Returns the difference between the solution and the target.

- **`POST /rachelriley/solve`**
    - **Description**: Finds a solution for the numbers round.
    - **Request Body**:
        - `target` (int): The target number.
        - `selection` (list): The list of selected numbers.
    - **Response**:
        - `200 OK`: Returns the solution.

### Conundrum Round

- **`GET /conundrumround/generate`**
    - **Description**: Generates a conundrum and its solution.
    - **Response**:
        - `200 OK`: Returns the conundrum and its solution.

- **`POST /conundrumround/validate`**
    - **Description**: Validates a solution for the conundrum.
    - **Request Body**:
        - `conundrum` (str): The conundrum.
        - `solution` (str): The solution to validate.
    - **Response**:
        - `200 OK`: Returns whether the solution is valid.

## Running Tests

To run the tests, use the following command:
```sh
python -m unittest discover tests