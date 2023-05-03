H, W = map(int, input().split())
A, B = [], []
for _ in range(H):
    A.append(input())
for _ in range(H):
    B.append(input())

yokoA = []
tateA = []

for i in range(H):
    cnt = 0
    for j in range(W):
        if A[i][j] == '#':
            cnt += 1
    yokoA.append(cnt)

for i in range(W):
    cnt = 0
    for j in range(H):
        if A[j][i] == '#':
            cnt += 1
    tateA.append(cnt)

yokoB = []
tateB = []

for i in range(H):
    cnt = 0
    for j in range(W):
        if B[i][j] == '#':
            cnt += 1
    yokoB.append(cnt)

for i in range(W):
    cnt = 0
    for j in range(H):
        if B[j][i] == '#':
            cnt += 1
    tateB.append(cnt)


flag_yoko = False
for i in range(H):
    shift_yokoB = []
    for j in range(H):
        shift_yokoB.append(yokoB[(i+j)%H])
    if yokoA == shift_yokoB:
        flag_yoko = True
        break


flag_tate = False
for i in range(W):
    shift_tateB = []
    for j in range(W):
        shift_tateB.append(tateB[(i+j)%W])
    if tateA == shift_tateB:
        flag_tate = True
        break

if flag_yoko and flag_tate:
    print('Yes')
else:
    print('No')

