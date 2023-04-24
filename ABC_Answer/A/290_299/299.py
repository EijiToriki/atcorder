N = int(input())
S = input()

pipe = []
aster = -1

for i in range(N):
    if S[i] == '|':
        pipe.append(i)
    if S[i] == '*':
        aster = i

if pipe[0] < aster < pipe[1]:
    print('in')
else:
    print('out')
