N, K = map(int, input().split())
S = input()

cnt1 = 0
for s in S:
    if s == '1':
        cnt1 += 1

if abs(cnt1 - K) % 2 == 0:
    print('Yes')
else:
    print('No')
