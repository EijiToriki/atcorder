def judge_prime_number(x):
    if x == 2:
        return True
    for i in range(2, int(x**0.5) + 2):
        if x % i == 0:
            return False
    return True

Q = int(input())
for _ in range(Q):
    x = int(input())
    if judge_prime_number(x):
        print('Yes')
    else:
        print('No')