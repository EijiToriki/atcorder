from itertools import permutations

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(2 ** (H+W-2)):
    pattern = []
    # 1 を縦、0 を横とする
    for j in range(H+W-2):
        if ((i >> j) & 1):
            pattern.append(1)
        else:
            pattern.append(0)
    if pattern.count(1) == H-1 and pattern.count(0) == W-1:
        check = set()
        h, w = 0, 0
        check.add(A[h][w])
        flag = True
        for p in pattern:
            if p == 0:
                w += 1
            else:
                h += 1
            if A[h][w] not in check:
                check.add(A[h][w])
            else:
                flag = False
                break
        if flag:
            ans += 1

print(ans)

            
