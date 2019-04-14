# Algorithm 4.24 from Handbook of Applied Cryptography
# Miller-Rabin probabilistic primality test
from random import randint

def miller_rabin(n, k=50):
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s = s + 1
        d = d >> 1
    for _ in range(k):
        a = randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                a = 0
                break
        if a:
            return False
    return True

def is_prob_prime(n):
	return miller_rabin(n)