#Algorithm 4.80 from Handbook of Applied Cryptography
from precompute import prime_factors
from gen_prime import test_alpha
import time

# verify_generator(2,32803350300091589) = True with runtime: 0.035787105560302734

def verify_generator(g,p):
	order_n = p-1
	start = time.time()
	primes = prime_factors(order_n)
	goodAlpha = test_alpha(g,order_n,primes)
	end = time.time()
	return goodAlpha,(end - start)


# if __name__ == "__main__":
# 	print(verify_generator(2,17428563951699683))