# Primes and generators
Experimenting with primes and generators. What are the different approaches to finding/testing primes and how do we efficiently verify generators? Main resource (free) used in order to understand and implement from pseudocode: [Handbook of Applied Cryptography](http://cacr.uwaterloo.ca/hac/). 

Entry point: [gen_prime.py](gen_prime.py)

# Instructions
Use gen_and_prime(primeDigits,safetyCheck) to return a prime of desired number of digits (and its associated generator) with the option to include a deterministic primality test.

# How it works

Once settling upon a safe prime P, find all prime factors for this prime. Take P-1 to be the order of P. For every prime Q in prime factors, see if an alpha (init as 2) is a valid generator by calculating the beta value via the formula:

```python
beta = alpha^(order/Q) % P
```

If beta value never returns 1 for any prime Q then it can be said that alpha is a valid generator for prime P.