import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

A, B, C = map(int, input().split())

gcd = my_gcd(A,B,C)
print(A//gcd-1 + B//gcd-1 + C//gcd-1)
