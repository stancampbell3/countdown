from susie_dent import is_valid_english_word, scoring

def test_is_valid_english_word():
    assert is_valid_english_word('mouse') == True

def test_proper_noun():
    assert is_valid_english_word('London') == False

def test_abbreviation():
    assert is_valid_english_word('UK') == False

def test_invalid_word():
    assert is_valid_english_word('swarzchbewgoooberOOooomelsh') == False

def test_single_letter():
    assert is_valid_english_word('a') == True

def test_scoring_1():
    assert scoring('mouse', 'cat') == [5, 3]

def test_scoring_2():
    assert scoring('123', 'cat') == [0, 3]

def test_scoring_3():
    assert scoring('mouse', '123') == [5, 0]

def test_scoring_4():
    assert scoring('123', '456') == [0, 0]

def test_scoring_5():
    assert scoring('astronaut', 'beautiful') == [18, 18]