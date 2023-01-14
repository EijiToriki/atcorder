def digit_sum(x):
  ans = 0
  while x > 0:
    ans += x % 10
    x = x // 10
  return ans


N, K = map(int, input().split())
mod = 10**5
next = []
for i in range(mod):
  next.append((i + digit_sum(i)) % mod)

time_stamp = [-1] * mod
pos, cnt = N, 0
while time_stamp[pos] == -1:
  time_stamp[pos] = cnt
  pos = next[pos]
  cnt += 1

cycle = cnt - time_stamp[pos]
if K >= time_stamp[pos]:
  K = (K - time_stamp[pos]) % cycle + time_stamp[pos]   ## ここの式がなぞ
ans = -1
for i in range(mod):
  if time_stamp[i] == K:
    ans = i

print(ans)