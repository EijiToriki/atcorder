from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

socks = defaultdict(int)

for a in A:
    socks[a] += 1

ans = 0
for v in socks.values():
    ans += v // 2

print(ans)
