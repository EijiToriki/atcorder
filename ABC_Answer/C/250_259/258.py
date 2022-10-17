N, Q = map(int, input().split())
S = input()

change_cnt = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        change_cnt += x
    if t == 2:
        print(S[x-change_cnt%N-1])