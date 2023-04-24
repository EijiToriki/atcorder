N = int(input())
S = input()

ans = -1
dango_cnt = 0
for i in range(N):
    if S[i] == 'o':
        dango_cnt += 1
    if S[i] == '-':
        ans = max(ans, dango_cnt)       
        dango_cnt = 0

S = S[::-1]
dango_cnt = 0
for i in range(N):
    if S[i] == 'o':
        dango_cnt += 1
    if S[i] == '-':
        ans = max(ans, dango_cnt)       
        dango_cnt = 0


if ans == 0:
    ans = -1
print(ans)