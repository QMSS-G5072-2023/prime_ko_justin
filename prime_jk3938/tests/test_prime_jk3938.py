# Contents of test_prime.py

import sys
sys.path.append("/Users/justin/Desktop/prime_ko_justin/prime_jk3938")

from src.prime_jk3938.prime_jk3938 import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(14) == False
