N = int(input())
S = input()

maru = 0
huka = 0
for i in range(N):
    if S[i] == 'o':
        maru += 1
    if S[i] == 'x':
        huka += 1

if maru >= 1 and huka == 0:
    print('Yes')
else:
    print('No')