'''
Algorithm 4.86 from Handbook of Applied Cryptography
Instructions: Use gen_and_prime(primeDigits,safetyCheck) to produce a prime of desired number of digits 
			  with the option to include a deterministic primality test.

How it works: Once settling upon a safe prime (P), find all prime factors for this prime. Take P-1 to be the order of P.
For every prime (Q) in prime factors, see if an alpha (init as 2) is a valid generator
by calculating the beta value via the formula:
beta = alpha^(order/Q) % our_prime

If beta value never returns 1 for any prime in the prime factors then it can be said that 
alpha is a valid generator for prime P.
'''
from test_prime import *
from find_prime import *
from precompute import prime_factors
from primality_test_basic import is_actual_prime
import random
import decimal
import time

# Prime: 32803350300091589, Length: 17, Gen: 2, Runtime: 0.038381099700927734

def safe_prime_gen(bits,safetyCheck):
	while True:
		q = find_prime(bits)
		p = is_prob_prime((2*q)+1)
		if p:
			# then it is a probable prime - do we want to run through
			# a deterministic test?
			if safetyCheck:
				p_2 = is_actual_prime(q,False)	
				if p_2: return q
			else:
				return q

def test_alpha(alpha,order_n,primes):
	our_prime = decimal.Decimal(order_n+1)
	for q in primes:
		print("Calculating exponential via {}/{}".format(order_n,q))
		exp_pi = decimal.Decimal(order_n)/decimal.Decimal(q)
		print("Calculating beta {}^{} % {} ".format(alpha,exp_pi,our_prime))
		b = pow(decimal.Decimal(alpha),exp_pi,our_prime)
		if b == 1:
			return False
	return True

def find_generator(our_prime):
	order_n = our_prime-1
	print("Finding primes...")
	primes = prime_factors(order_n)
	print(primes)
	print("Primes found and continuing...")

	alpha = 1
	goodAlpha = False
	while goodAlpha != True:
		alpha += 1
		print("Testing for alpha {}".format(alpha))
		goodAlpha = test_alpha(alpha,order_n,primes)
		if alpha == order_n:
			alpha = 0
			return 
		
	return alpha

def gen_and_prime(prime_digits,safetyCheck):
	prime_bits = len(bin(10 ** (prime_digits-1))[2:])
	start = time.time()
	chosen_prime = safe_prime_gen(prime_bits+1,safetyCheck)
	prime_found_len = len(str(chosen_prime))
	while prime_found_len != 17:
		chosen_prime = safe_prime_gen(prime_bits+1,safetyCheck)
		prime_found_len = len(str(chosen_prime))
	generator = find_generator(chosen_prime)
	end = time.time()
	print("Prime: {}, Length: {}, Gen: {}, Runtime: {}".format(chosen_prime,
		len(str(chosen_prime)),generator,(end - start)))
	return chosen_prime,generator
	
# if __name__ == "__main__":
# 	prime,generator = gen_and_prime(17,False)
