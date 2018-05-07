def is_prime(n):
    """Returns True is number is prime, and false otherwise."""
    
    counter = 2
    if n < counter:
        return False
    while counter < n:
        if n%counter == 0:
            return False
        else:
            counter+=1
    return True
 
