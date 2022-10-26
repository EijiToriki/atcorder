import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

que = P[0:K]
print(min(que))
heapq.heapify(que)

for i in range(K, N):
  minima = heapq.heappop(que) ## 最小値の取り出し
  minima = max(minima, P[i])
  heapq.heappush(que, minima)
  ans = heapq.heappop(que)
  print(ans)
  heapq.heappush(que, ans)


# p_set = set()
# min = 10**6
# for i in range(K):
#   if min > P[i]:
#     min = P[i]
#   p_set.add(P[i])

# ans = min
# print(ans)

# for i in range(K, N):
#   if P[i] > ans:
#     while True:
#       ans += 1
#       if ans in p_set:
#         break
  
#   p_set.add(P[i])
#   print(ans)  