import wn

en_wordnet = wn.Wordnet('oewn:2024')

def scoring(team1_word, team2_word):
    len_word1 = len(team1_word)
    len_word2 = len(team2_word)
    if len_word1 == 9:
        points1 = 18
    else:
        points1 = len_word1

    if len_word2 == 9:
        points2 = 18
    else:
        points2 = len_word2

    valid1 = is_valid_english_word(team1_word)
    valid2 = is_valid_english_word(team2_word)
    if not valid1:
        points1 = 0
    if not valid2:
        points2 = 0
    return [points1, points2]

def is_valid_english_word(word):
    test_word = word.lower()

    if len(test_word) == 1 and (test_word == 'a' or test_word == 'i'):
        return True

    synsets = en_wordnet.synsets(test_word)
    if not synsets:
        return False

    for synset in synsets:
        if synset.pos =='n': # noun
            lemmas = synset.lemmas()
            for lemma in lemmas:
                if lemma.istitle():
                    return False

    # heuristic for abbreviations, needs work
    if test_word.isupper() and len(test_word) > 1:
        return False

    return True

