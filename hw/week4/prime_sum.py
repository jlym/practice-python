import prime

def sum_of_primes(n):
    """Returns the sum of all prime numbers between 1 and n (not inclusive)."""
    sum = 0
    for num in range(1,n):
        if prime.is_prime(num) == True:
            sum += num
    return sum