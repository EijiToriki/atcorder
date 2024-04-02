N, D, P = map(int, input().split())
F = sorted(list(map(int, input().split())))

one_day_price = P / D
larger_date = 0
for f in F:
  if one_day_price < f:
    larger_date += 1

ticket = larger_date // D
total1 = ticket * P
for i in range(len(F)-D*ticket):
  total1 += F[i]

ticket += 1
total2 = ticket * P
for i in range(len(F)-D*ticket):
  total2 += F[i]

ans = min(total1, total2)
print(ans)