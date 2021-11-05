n = input('Show prime numbers up to: ')
i = 3
prime_numbers = [2]
poss_primes = []
while i < int(n):
    for primes in prime_numbers:
        poss_primes.append(i % primes)
    if not any(poss_prime == 0 for poss_prime in poss_primes):
        prime_numbers.append(i)
    poss_primes.clear()
    i += 1
f = open('primes.txt', 'w+')
for prime in prime_numbers:
     f.write(str(prime) + '\r\t')
f.close()
import os
file = 'primes.txt'
os.system(file)
