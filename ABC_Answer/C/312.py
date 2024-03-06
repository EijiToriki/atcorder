from bisect import bisect_right

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

for a in A:
  print(a, bisect_right(B, a))

