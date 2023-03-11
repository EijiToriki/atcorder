from itertools import permutations

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

grid = []
for _ in range(H-1):
    grid.append(0)

for _ in range(W-1):
    grid.append(1)

a = set()
for comb in list(permutations(grid)):
    a.add(comb)

a = list(a)

ans = 0
for b in a:
    flag = True
    l = [A[0][0]]
    h = 0
    w = 0
    for c in b:
        if c == 0:
            h += 1
        else:
            w += 1
        if A[h][w] in l:
            flag = False
            break
        l.append(A[h][w])
    if flag:
        ans += 1

print(ans)
