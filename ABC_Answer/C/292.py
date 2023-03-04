def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])

N = int(input())

ans = 0
for i in range(1, N + 1):
    ans += make_divisors(i) * make_divisors(N-i)
    
print(ans)

