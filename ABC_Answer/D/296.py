## TLE するやつ
# def make_divisors(n):
#     lower_divisors = []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#         i += 1
#     return lower_divisors



# N, M = map(int, input().split())
# max_val = N * N

# if max_val < M :
#     print(-1)
#     exit()

# for m in range(M, max_val+1):
#     divs = make_divisors(m)
#     for a in divs:
#         b = m // a
#         if a <= N and b <= N:
#             print(m)
#             exit()

# print(-1)


## なぜか WA
# import math

# N, M = map(int, input().split())
# ans = float('INF')

# for a in range(1, int(math.sqrt(M))+1):
#     if M % a == 0:
#         b = M // a
#     else:
#         b = int(M / a) + 1

#     if a <= N and b <= N:
#         ans = min(a*b, ans)

# if ans == float('INF'):
#     print(-1)
# else:
#     print(ans)


N, M = map(int, input().split())
x = 0
ans = float('INF')

for a in range(1, N+1):
    b = (M+a-1) // a
    if b <= N:
        ans = min(ans, a*b)
    if a > b:
        break

if ans == float('INF'):
    print(-1)
else:
    print(ans)