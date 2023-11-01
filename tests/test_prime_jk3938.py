
# Contents of test_prime.py

from prime_jk3938 import prime_jk3938
import math

import pytest
from is_prime import is_prime, generate_primes

def test_is_prime():
    # Known prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in prime_numbers:
        assert is_prime(prime) == True, f"Test failed with {prime}"
    
    # Known composite numbers
    composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
    for composite in composite_numbers:
        assert is_prime(composite) == False, f"Test failed with {composite}"
    
    # Edge cases
    assert is_prime(0) == False, "Test failed with 0"
    assert is_prime(1) == False, "Test failed with 1"
    assert is_prime(-5) == False, "Test failed with -5"


@pytest.mark.parametrize(
    "number, expected", [
        (2, True),  # prime
        (3, True),  # prime
        (4, False),  # composite
        (5, True),  # prime
        (6, False),  # composite
        (7, True),  # prime
        (8, False),  # composite
        (9, False),  # composite
        (10, False),  # composite
        (0, False),  # edge case
        (1, False),  # edge case
        (-5, False),  # edge case (negative number)
    ]
)
def test_is_prime_param(number, expected):
    assert is_prime(number) == expected, f"Test failed with {number}"


def test_generate_primes():
    # Typical cases
    assert generate_primes(10) == [2, 3, 5, 7], "Test failed with limit 10"
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Test failed with limit 20"

    # Edge cases
    assert generate_primes(0) == [], "Test failed with limit 0"
    assert generate_primes(1) == [], "Test failed with limit 1"
    assert generate_primes(-5) == [], "Test failed with limit -5"
    assert generate_primes(2) == [2], "Test failed with limit 2"
    
    # Larger case
    assert generate_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test failed with limit 30"

    
def test_prime_integration():
    # Generate a list of prime numbers up to a certain limit
    limit = 30
    prime_list = generate_primes(limit)
    
    # Check the correctness of each prime number using the is_prime function
    for prime in prime_list:
        assert is_prime(prime) == True, f"Test failed with {prime}"
    
    # Additional check: Ensure there are no false negatives
    for i in range(2, limit + 1):
        if i not in prime_list:
            assert is_prime(i) == False, f"Test failed with {i}, false negative"


