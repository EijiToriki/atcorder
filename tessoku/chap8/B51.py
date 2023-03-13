from collections import deque

S = input()

Bracket = deque()
ans = []
for i in range(len(S)):
    if S[i] == '(':
        Bracket.append(i+1)
    else:
        l = Bracket.pop()
        r = i+1
        ans.append([l, r])

for one_ans in ans:
    print(*one_ans)