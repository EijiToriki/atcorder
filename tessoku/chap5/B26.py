def judge_prime_number(x):
    if x == 2:
        return True
    for i in range(2, int(x**0.5) + 2):
        if x % i == 0:
            return False
    return True

N = int(input())
for i in range(2, N+1):
    if judge_prime_number(i):
        print(i)