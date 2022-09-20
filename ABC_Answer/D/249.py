def make_divisors(n):
    ans_part = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            small = A_cnt[i]
            if n // i != i:
                big = A_cnt[n//i]
                ans_part += small * big * 2
            else:
                ans_part += small ** 2

    return ans_part


N = int(input())
A = list(map(int, input().split()))
A_cnt = [0 for _ in range(max(A)+1)]

for a in A:
    A_cnt[a] += 1

ans = 0
for a in A:
    ans += make_divisors(a)

print(ans)
