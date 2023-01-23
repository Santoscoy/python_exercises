"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following
form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def prime_factors(n):
    primes_numbers = prime_numbers_calculator(n)
    return operation_builder(primes_numbers)


def operation_builder(prime_numbers):
    operation = ''
    for k, v in prime_numbers.items():
        operation += f'({k}**{v})' if v != 1 else f'({k})'
    return operation


def prime_numbers_calculator(n):
    results = {}
    divisor = 2
    count = 0
    while n > 1:
        if n % divisor == 0:
            count += 1
            results[divisor] = count
            n = n / divisor
        else:
            count = 0
            divisor += 1
    return results

if __name__ == '__main__':  # noqa
    print(prime_factors(7775460))  # should return  "(2**2)(3**3)(5)(7)(11**2)(17)"
    print(prime_factors(7919))  # should return  "(7919)"
