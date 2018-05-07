import prime
import prime_sum as ps

#Tests for prime.
def test_0_is_not_prime():
    assert prime.is_prime(0) is False, "0 is not a prime number"

def test_2_is_prime():
    assert prime.is_prime(2) is True, "2 is a prime number"
    
#Tests for sum of primes.
def test_1_sum_of_prime():
    assert ps.sum_of_primes(1) is 0, "Sum of primes for 1 is zero"
    
def test_4_sum_of_prime():
    assert ps.sum_of_primes(4) is 5, "Sum of primes for 4 is five"
    
def test_5_sum_of_prime():
    assert ps.sum_of_primes(5) is 5, "Sum of primes for 5 is five"