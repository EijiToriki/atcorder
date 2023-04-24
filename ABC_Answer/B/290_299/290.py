N, K = map(int, input().split())
S = input()

maru_cnt = 0
ans = []
for s in S:
    if s == 'o' and maru_cnt < K:
        ans.append('o')
        maru_cnt += 1
    else:
        ans.append('x')

ans = ''.join(ans)
print(ans)