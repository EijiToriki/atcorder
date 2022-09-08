import math

def make_divisors(n, limit):
    lower_divisors, upper_divisors = [], []
    i = math.floor(math.sqrt(n))
    while i > 0:
        if n % i == 0:
            if i<= limit and n//i <= limit:
                lower_divisors.append(i)
                if i != n//i:
                    upper_divisors.append(n//i)
            else:
                break
        i -= 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
square_list = [i*i for i in range(1, N+1)]

ans = 0
for n in square_list:
    ans += len(make_divisors(n, N))

print(ans)
