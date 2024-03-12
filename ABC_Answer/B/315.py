M = int(input())
D = list(map(int, input().split()))

mannaka = (sum(D) + 1) // 2

for i, d in enumerate(D):
  mannaka -= d
  if mannaka <= 0:
    a = i+1
    b = mannaka + d
    print(a, b)
    exit()