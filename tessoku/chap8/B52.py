from collections import deque

N, X = map(int, input().split())
A = list(input())

q = deque([X-1])
A[X-1] = '@'
while len(q) != 0:
    pos = q.popleft()
    if pos-1 >= 0:
        if A[pos-1] == '.':
            A[pos-1] = '@'
            q.append(pos-1)
    if pos+1 < N:
        if A[pos+1] == '.':
            A[pos+1] = '@'
            q.append(pos+1)

ans = ''.join(A)
print(ans)