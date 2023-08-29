# wordlist_generator.py
import random
import string

def generate_wordlist(num_common=50, num_random=5000):
    common_words = ["password", "123456", "qwerty", "letmein", "admin", "123456789", "welcome"]
    wordlist = common_words[:num_common]

    random_words = [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(5, 15))) for _ in range(num_random)]
    wordlist.extend(random_words)

    return wordlist
