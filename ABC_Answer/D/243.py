N, X = map(int, input().split())
S = input()

ans = X
over_cnt = 0

for i in range(N):
    if ans <= 10**18 and over_cnt == 0:
        if S[i] == 'U':
            ans = ans // 2
        if S[i] == 'L':
            ans = ans * 2
        if S[i] == 'R':
            ans = ans * 2 + 1
        if ans > 10**18:
            over_cnt += 1
    else:
        if S[i] == 'U':
            over_cnt -= 1
        else:
            over_cnt += 1
        if over_cnt == 0:
            ans = ans // 2

print(ans)