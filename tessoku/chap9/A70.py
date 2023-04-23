import copy
from collections import defaultdict, deque

# 10進 → 2進
def change_binary(num, N):
    rslt = []
    num = bin(num)[2:]
    for _ in range(N-len(num)):
        rslt.append('0')
    for n in num:
        rslt.append(n)

    return rslt


# グラフの遷移
def next_state(binary_i, op):
    buf = copy.copy(binary_i)
    buf[op[0]-1] = str(1 - int(buf[op[0]-1]))
    buf[op[1]-1] = str(1 - int(buf[op[1]-1]))
    buf[op[2]-1] = str(1 - int(buf[op[2]-1]))
    return buf


# 2進 → 10進
def change_decimal(binary):
    rslt = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            rslt += 2 ** (len(binary)-i-1)
    return rslt


# 入力受取
N, M = map(int, input().split())
A = list(input().split())
opes = []
for _ in range(M):
    x, y, z = map(int, input().split())
    opes.append((x, y, z))


# グラフの辺追加
G = [[] for _ in range(2**N)]
for i in range(2 ** N):
    binary_i = change_binary(i, N)
    for op in opes:
        G[change_decimal(binary_i)].append(change_decimal(next_state(binary_i, op)))


# 初期値設定
start = change_decimal(A)
goal = 2 ** N - 1

dist = [-1] * (2 ** N)
dist[start] = 0

que = deque()
que.append(start)

while(len(que)!=0):
    v = que.popleft()

    for next in G[v]:
        if dist[next] != -1:
            continue
        dist[next] = dist[v] + 1
        que.append(next)


print(dist[goal])
