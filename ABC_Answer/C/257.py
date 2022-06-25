import bisect

N = int(input())
S = input()
W = list(map(int, input().split()))

adult_weight = []
child_weight = []

for i,w in enumerate(W):
    if S[i] == '0':
        child_weight.append(w)
    else:
        adult_weight.append(w)

child_weight = sorted(child_weight)
adult_weight = sorted(adult_weight)

adult_num = len(adult_weight)
chilid_num = len(child_weight)

ans = 0

for i,w in enumerate(W):
    robot = 0
    robot += adult_num - bisect.bisect_left(adult_weight, w+0.1)
    robot += bisect.bisect_left(child_weight, w+0.1)
    if ans < robot:
        ans = robot

    robot = 0
    robot += adult_num - bisect.bisect_left(adult_weight, w)
    robot += bisect.bisect_left(child_weight, w)
    if ans < robot:
        ans = robot

    robot = 0
    robot += adult_num - bisect.bisect_left(adult_weight, w-0.1)
    robot += bisect.bisect_left(child_weight, w-0.1)
    if ans < robot:
        ans = robot

print(ans)