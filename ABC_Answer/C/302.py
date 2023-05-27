from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

s_num = [i for i in range(N)]

ans_flag = False
for pat in list(permutations(s_num)):
    clear = 0
    for i in range(1, N):
        diff = 0
        for j in range(M):
            if S[pat[i-1]][j] != S[pat[i]][j]:
                diff += 1
        if diff == 1:
            clear += 1
    if clear == N-1:
        ans_flag = True


if ans_flag:
    print('Yes')
else:
    print('No')


