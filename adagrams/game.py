import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

LETTER_VALUES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10 
}
def draw_letters():
    letters = []
    while len(letters) < 10:
        letter = random.choice(list(LETTER_POOL.keys()))
        if letters.count(letter) < LETTER_POOL[letter]:
            letters.append(letter)
    return letters

def uses_available_letters(word, letter_bank):
    '''
    (1) read letter from word (in list) from user
    (2) read letter_bank from the output of draw_letters()
    (3) check if each letter in the letter_bank
    '''

    letters = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in letters:
            letters.remove(letter)
            continue
        else:
            return False
    return True

def score_word(word):
    '''
    (1) letter in word
    (2) get the value from LETTER_VALUES (in dict)
    (3) add each value to score
    '''

    score = 0
    word = word.upper()
    for letter in word:
        score += LETTER_VALUES[letter]
        
    if len(word) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    pass
