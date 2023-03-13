from collections import deque

Q = int(input())

q = deque()
for _ in range(Q):
    query = list(input().split())
    if query[0] == '1':
        q.append(query[1])
    elif query[0] == '2':
        print(q[0])
    else:
        q.popleft()
