N = int(input())
P1 = [0] + [0 for _ in range(N)]
P2 = [0] + [0 for _ in range(N)]
for i in range(1, N+1):
  c,p = map(int, input().split())
  if c == 1:
    P1[i] = P1[i-1] + p
    P2[i] = P2[i-1]
  else:
    P1[i] = P1[i-1]
    P2[i] = P2[i-1] + p
  
Q = int(input())
for _ in range(Q):
  l,r = map(int, input().split())
  class1_score = P1[r] - P1[l-1]
  class2_score = P2[r] - P2[l-1]

  print(*[class1_score, class2_score])

