import random
from test_prime import *

def find_prime(n,k=50):
	find_prime = True
	while find_prime:
		random_num = int(random.getrandbits(n))
		if random_num % 2 == 0:
			random_num += 1

		if is_prob_prime(random_num):
			find_prime = False
			return random_num