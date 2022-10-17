N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
  if A[i] == i+1:
    cnt += 1

ans = (cnt-1)*cnt // 2

cnt = 0
for i in range(N):
  if A[A[i]-1] == i+1 and A[i] != i+1:
    cnt += 1

ans += cnt // 2
print(ans)