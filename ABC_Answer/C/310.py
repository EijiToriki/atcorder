N = int(input())

ans = 0
bar_set = set()
for _ in range(N):
  Si = input()
  reversed_Si = Si[::-1]
  if not (Si in bar_set or reversed_Si in bar_set):
    bar_set.add(Si)
    bar_set.add(reversed_Si)
    ans += 1

print(ans)