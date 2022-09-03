# import sys
# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# S = [0]*(N+1)
# for i in range(N):
#     S[i+1] = S[i] + A[i] * (i+1)

# max_val = -sys.maxsize
# max_index = 0
# for i in range(1, N-M+1):
#     if max_val < S[i+M]-S[i]:
#         max_index = i
#         max_val = S[i+M]-S[i]

# ans = 0
# for i in range(M):
#     ans += (i+1)*A[max_index+i]

# print(ans)

import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

max_val = -sys.maxsize
for i in range(N-M+1):
    val = 0
    cnt = 1
    for j in range(i, i+M):
        val +=  cnt * A[j]
        cnt += 1
        
    if ans < val:
        ans = val

print(ans)