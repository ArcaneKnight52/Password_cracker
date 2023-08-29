# dictionary_attack.py
import hashlib

def dictionary_attack(hashed_password, wordlist):
    for word in wordlist:
        for algo in hashlib.algorithms_available:
            hashed_word = hashlib.new(algo, word.encode()).hexdigest()
            if hashed_word == hashed_password:
                return word, algo
    return None, None
