from ctypes.wintypes import WORD
from operator import mul
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
    '''Create letter bank from letter pool. Letters cannot repeat more than values in letter pool.'''
    
    # refactored code to make function more efficient -- getting list of letter pool keys once
    # and not counting each letter with every iteration 
    letters = list(LETTER_POOL.keys())
    hand = []
    letter_count = {}

    while len(hand) < 10:
        letter = random.choice(letters)
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

        if letter_count[letter] < LETTER_POOL[letter]:
            hand.append(letter)

    return hand

    # original code
    # letters = []
    # while len(letters) < 10:
    #     letter = random.choice(list(LETTER_POOL.keys()))
    #     if letters.count(letter) < LETTER_POOL[letter]:
    #         letters.append(letter)
    # return letters     
        

def uses_available_letters(word, letter_bank):
    '''Check if letters and repeated letters in word are in letterbank'''

    letters = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in letters:
            letters.remove(letter)
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
    '''Return word with highest score using tie-breaking rules:
        - prefer the word with the fewest letters
        - unless one word has 10 letters, word with 10 letters wins
        - if multiple words that are the same score and the same length, pick the 
        first one in the supplied list'''

    # code after refactor

    # create dict with words with their scores
    words_with_score = {}
    for word in word_list:
        word_score = score_word(word)
        words_with_score[word] = word_score

    max_score = max(words_with_score.values())
    
    # create dict of all words with max score
    max_score_words = {}

    for word in words_with_score:
        if max_score <= words_with_score[word]:
            max_score_words[word] = words_with_score[word]

    # find word with highest score using tie-breaking rules
    winning_word = ()
    length_of_winning_word = 10
    for word in max_score_words:
        if len(word) == 10: # returns the first word with 10 letters
            return (word, max_score_words[word])
        elif len(word) < length_of_winning_word: # returns the first word with shortest length by using < rather than <=
            length_of_winning_word = len(word)
            winning_word = (word, max_score_words[word])
    
    return winning_word
        
    # original code
    # words_with_scores = {}
    # for word in word_list:
    #     score = score_word(word)
    #     words_with_scores[word] = score
    
    # highest_score_word = max(words_with_scores,key=words_with_scores.get) 
    # high_score = words_with_scores[highest_score_word]

    # max_score_tuple = (highest_score_word, words_with_scores[highest_score_word])
    
    # multiple_max_score_words = []
    # for key in words_with_scores:
    #     if high_score == words_with_scores[key]:
    #         multiple_max_score_words.append(key)

    # if len(multiple_max_score_words) == 1:
    #     return max_score_tuple
    # else:
    #     for i in range(0, len(multiple_max_score_words)):
    #         if len(multiple_max_score_words[i]) == 10:
    #             return (multiple_max_score_words[i], words_with_scores[multiple_max_score_words[i]])
    #         elif len(multiple_max_score_words[i-1]) < len(multiple_max_score_words[i]):
    #             current_winner = (multiple_max_score_words[i-1], words_with_scores[multiple_max_score_words[i-1]]) 
    #         else:
    #             current_winner = (multiple_max_score_words[i], words_with_scores[multiple_max_score_words[i]])

    # return current_winner  


