XY = input()
X, Y = XY.split('.')

if 0 <= int(Y) <= 2:
  ans = X + '-'
elif 3 <= int(Y) <= 6:
  ans = X
else:
  ans = X + '+'

print(ans)