# hash_attack.py
import hashlib

def hash_attack(target_password, input_password, hash_algorithm):
    if hash_algorithm in hashlib.algorithms_available:
        return hashlib.new(hash_algorithm, input_password.encode()).hexdigest() == target_password
    else:
        raise ValueError("Unsupported hash algorithm")
