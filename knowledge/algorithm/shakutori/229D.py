S = input()
K = int(input())

cnt = [0] * (len(S)+1)
for i in range(len(S)):
  if S[i] == '.':
    cnt[i+1] = cnt[i] + 1
  else:
    cnt[i+1] = cnt[i]


ans = 0
r = 0
for l in range(len(S)):
  while r <= len(S)-1 and cnt[r+1]-cnt[l] <= K:
    r += 1
  ans = max(ans, r-l)

print(ans)