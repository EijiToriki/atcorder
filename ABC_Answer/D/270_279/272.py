from math import ceil, sqrt
from collections import deque

def judge(k, l):
    if 0 <= k < N and 0 <= l < N:
        return True
    else:
        return False

def update_ans_check_next(k, l):
    check[k][l] = True
    ans[k][l] = ans_cnt
    next.append([k, l])  


N, M = map(int, input().split())

kl_candi = [x**2 for x in range(ceil(sqrt(M))+1)]

pairs = []
for k in kl_candi:
    for l in kl_candi:
        if k + l == M and k <= l:
            pairs.append([int(sqrt(k)), int(sqrt(l))])

ans = [[-1] * N  for _ in range(N)]
check = [[False] * N for _ in range(N)]
ans[0][0] = 0
check[0][0] = True

next = deque([[0,0]])
ans_cnt = 1
now_cnt = 0
next_len = len(next)
while len(next) != 0:
    now = next.popleft()
    now_cnt += 1
    for pair in pairs:
        k1, l1 = now[0] + pair[0], now[1] + pair[1]
        k2, l2 = now[0] + pair[0], now[1] - pair[1]
        k3, l3 = now[0] - pair[0], now[1] + pair[1]
        k4, l4 = now[0] - pair[0], now[1] - pair[1]
        k5, l5 = now[0] + pair[1], now[1] + pair[0]
        k6, l6 = now[0] + pair[1], now[1] - pair[0]
        k7, l7 = now[0] - pair[1], now[1] + pair[0]
        k8, l8 = now[0] - pair[1], now[1] - pair[0]

        if judge(k1, l1) and (not check[k1][l1]):
            update_ans_check_next(k1, l1)
        if judge(k2, l2) and (not check[k2][l2]):
            update_ans_check_next(k2, l2)
        if judge(k3, l3) and (not check[k3][l3]):
            update_ans_check_next(k3, l3)
        if judge(k4, l4) and (not check[k4][l4]):
            update_ans_check_next(k4, l4)
        if judge(k5, l5) and (not check[k5][l5]):
            update_ans_check_next(k5, l5)
        if judge(k6, l6) and (not check[k6][l6]):
            update_ans_check_next(k6, l6)
        if judge(k7, l7) and (not check[k7][l7]):
            update_ans_check_next(k7, l7)
        if judge(k8, l8) and (not check[k8][l8]):
            update_ans_check_next(k8, l8)



    if now_cnt == next_len:
        now_cnt = 0
        next_len = len(next)
        ans_cnt += 1

for ans_row in ans:
    print(*ans_row)