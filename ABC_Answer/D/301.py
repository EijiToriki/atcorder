S = input()
N = int(input())

ans = 0
bit1 = []
for i in range(len(S)):
    if S[i] == '1':
        ans += 2**(len(S)-i-1)

if ans > N:
    print(-1)
    exit()

for i in range(len(S)):
    if S[i] == '?':
        if ans + 2**(len(S)-i-1) <= N:
            ans += 2**(len(S)-i-1)

print(ans)
