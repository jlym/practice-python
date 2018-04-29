import prime

def test_0_is_not_prime():
    assert prime.is_prime(0) is False, "0 is not a prime number"

def test_2_is_prime():
    assert prime.is_prime(2) is True, "2 is a prime number"
    
