N, K = map(int, input().split())
A = list(map(int, input().split()))

if len(A) <= K:
  ans = [0] * N
else:
  ans = A[K:] + [0] * K

print(*ans)