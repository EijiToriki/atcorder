N = int(input())
magic_num = 998244353

sho = abs(N) // magic_num

if N >= 0:
  ans = N - sho * magic_num
else:
  ans = N + (sho + 1) * magic_num
  if ans == magic_num:
    ans = 0

print(ans)
