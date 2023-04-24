N = int(input())
S = input()

flag = True
prev = S[0]
for i in range(1, N):
    if prev != S[i]:
        prev = S[i]
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')
