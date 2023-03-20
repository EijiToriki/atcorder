from collections import defaultdict

N, Q = map(int, input().split())

wait = defaultdict(int)
e1 = 1
for _ in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        wait[e1] = 1
        e1 += 1
    elif event[0] == 2:
        del wait[event[1]]
    else:
        print(next(iter(wait)))


