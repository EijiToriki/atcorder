# import numpy as np
# from numpy import linalg as LA

# A  = list(map(int, input().split()))
# B  = list(map(int, input().split()))
# C  = list(map(int, input().split()))
# D  = list(map(int, input().split()))

# def two_vector_angle(u, v):
#   u = np.array(u)
#   v = np.array(v)

#   i = np.inner(u, v)
#   n = LA.norm(u) * LA.norm(v)
#   c = i / n
#   return np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))


# AB = [B[0]-A[0], B[1]-A[1]]
# BC = [C[0]-B[0], C[1]-B[1]]
# CD = [D[0]-C[0], D[1]-C[1]]
# DA = [A[0]-D[0], A[1]-D[1]]


# ABtoBC = two_vector_angle(AB, BC)
# BCtoCD = two_vector_angle(BC, CD)
# CDtoDA = two_vector_angle(CD, DA)
# DAtoAB = two_vector_angle(DA, AB)

# if sum([ABtoBC, BCtoCD, CDtoDA, DAtoAB]) == 360:
#   print('Yes')
# else:
#   print('No')

N = int(input())
txa = [list(map(int, input().split())) for _ in range(N)]
max_time = txa[N-1][0]

dp = [[0 for _ in range(5)] for _ in range(max_time+1)]

h = 0
for i in range(1, max_time+1):
  if i == txa[h][0]:
    for j in range(min(i+1, 5)):
      if j == txa[h][1]:
        if j == 0:
          dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1]) + txa[h][2]
        elif j == 4:
          dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j]) + txa[h][2]
        else:
          dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + txa[h][2]

      if j == 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1])
      elif j == 4:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j])
      else:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    h += 1
  else:
    for j in range(min(i+1, 5)):
      if j == 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1])
      elif j == 4:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j])
      else:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

print(max(dp[max_time]))  
