N = int(input())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

ans = 0
now = 0
for a, b in AB:
    if a + b > 0:
        now += (a + b)
ans = max(ans, now)

now = 0
for a, b in AB:
    if a - b > 0:
        now += (a - b)
ans = max(ans, now)

now = 0
for a, b in AB:
    if - a + b > 0:
        now += (- a + b)
ans = max(ans, now)

now = 0
for a, b in AB:
    if - a - b > 0:
        now += (- a - b)
ans = max(ans, now)

print(ans)