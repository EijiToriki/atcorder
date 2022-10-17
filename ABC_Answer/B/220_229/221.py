S = list(input())
T = list(input())

if S == T:
    print('Yes')
    exit()

for i in range(len(S)-1):
    S_copy = S.copy()
    S_copy[i], S_copy[i+1] = S_copy[i+1], S_copy[i]
    if S_copy == T:
        print('Yes')
        exit()

print('No')
