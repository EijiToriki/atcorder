N = int(input())
A = list(map(int, input().split()))

f = [-1 for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

for i, a in enumerate(A):
  cnt[a] += 1
  if cnt[a] == 2:
    f[a] = i

f = f[1:]

ans = sorted(range(len(f)),key=f.__getitem__)
ans = [a+1 for a in ans]

print(*ans)