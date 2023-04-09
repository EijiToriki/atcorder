from collections import deque

N = int(input())
A = list(map(int, input().split()))

kisan_stack = deque()
ans = [-1] * N
for d in range(1, N):
    kisan_stack.append((d, A[d-1]))

    while len(kisan_stack) != 0:
        if kisan_stack[-1][1] < A[d]:
            kisan_stack.pop()
        else:
            break
    
    if len(kisan_stack) != 0:
        ans[d] = kisan_stack[-1][0]

print(*ans)
