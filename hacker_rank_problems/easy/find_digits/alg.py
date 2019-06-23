"""Taken from https://www.hackerrank.com/challenges/find-digits/problem"""


def find_digits(d: int) -> int:
    total_divisors: int = 0
    str_d = str(d).replace('0', '')
    for num_str in str_d:
        num = int(num_str)
        if d % num == 0:
            total_divisors += 1
    return total_divisors
