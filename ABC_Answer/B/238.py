N = int(input())
A = list(map(int, input().split()))

kirikomi = []

now_kakudo = 0
kirikomi.append(now_kakudo)
kirikomi.append(360)

for i in range(N):
  now_kakudo = (now_kakudo + A[i]) % 360
  kirikomi.append(now_kakudo)

kirikomi = list(set(kirikomi))
kirikomi = sorted(kirikomi)


ans = []
for i in range(N+1):
  ans.append(kirikomi[i+1] - kirikomi[i])

print(max(ans))