# brute_force_attack.py
import hashlib
import itertools
import string
import time

def generate_charset():
    charset = string.ascii_letters + string.digits + string.punctuation
    return charset

def brute_force_attack(hashed_password, charset, max_length):
    start_time = time.time()

    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            password = "".join(combination)
            for algo in hashlib.algorithms_guaranteed:
                hashed_password_attempt = hashlib.new(algo, password.encode()).hexdigest()
                if hashed_password_attempt == hashed_password:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    return password, elapsed_time, algo

    return None, None, None
