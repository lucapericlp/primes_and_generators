import time
import math

# is_actual_prime(2685735182217719) = True with runtime: 3.8483729362487793
#                                     and 8,637,346 iterations till completion
def checkComplexity(counter,n):
    theory = math.sqrt(n)//6
    return (counter == theory)

def is_actual_prime(n,withComplexity):
    counter = 0
    if n <= 3:
        return n >= 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        counter += 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    if withComplexity:
        return True,checkComplexity(counter,n)
    else:
        return True

if __name__ == "__main__":
    start = time.time()
    result,complexity = is_actual_prime(2685735182217719,True)
    end = time.time()
    print(result,complexity,end - start)