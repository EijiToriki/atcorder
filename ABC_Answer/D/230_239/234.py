import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

p_set = set()
min = 10**6
for i in range(K):
  if min > P[i]:
    min = P[i]
  p_set.add(P[i])

ans = min
print(ans)

for i in range(K, N):
  p_set.add(P[i])
  if P[i] > ans:
    while True:
      ans += 1
      if ans in p_set:
        break
  
  print(ans)  