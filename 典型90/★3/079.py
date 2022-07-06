# 問題の主旨は，どのマスから見ても結局変わらないということ
# だが，H, Wがごちゃついて苦戦した

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

query_num = 0
for i in range(H-1):
    for j in range(W-1):
        diff = B[i][j] - A[i][j]
        query_num += abs(diff)
        A[i][j] += diff
        A[i+1][j] += diff
        A[i][j+1] += diff
        A[i+1][j+1] += diff

flag = True
for i in range(H):
    for j in range(W):
        if A[i][j] != B[i][j]:
            flag = False
            break
if flag:
    print('Yes')
    print(query_num)
else:
    print('No')