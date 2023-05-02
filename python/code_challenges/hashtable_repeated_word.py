from data_structures.hashtable import Hashtable
import re

def first_repeated_word(sentence):
    words = sentence.split()
    hash_table = Hashtable(len(words) * 10)
    for word in words:
        lowered_word = word.lower()
        normalized_word = re.sub('[^A-Z]', "", lowered_word, 0, re.IGNORECASE)
        if hash_table.has(normalized_word):
            print('has', normalized_word)
            return normalized_word
        else:
            hash_table.set(normalized_word, word)
    return None

if __name__ == '__main__':
    first_repeated_word("nobody here but us chickens")

