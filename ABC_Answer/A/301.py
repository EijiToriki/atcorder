N = int(input())
S = input()

A_last = -1
T_last = -1

A_cnt = 0
T_cnt = 0

for i in range(N):
    if S[i] == 'A':
        A_last = i
        A_cnt += 1
    if S[i] == 'T':
        T_last = i
        T_cnt += 1

if A_cnt > T_cnt:
    print('A')
elif A_cnt < T_cnt:
    print('T')
else:
    if A_last > T_last:
        print('T')
    else:
        print('A')
