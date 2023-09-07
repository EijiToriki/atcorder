N = int(input())
S = input()

ans = []
for i in range(2*N):
  ans.append(S[i//2])

print(''.join(ans))