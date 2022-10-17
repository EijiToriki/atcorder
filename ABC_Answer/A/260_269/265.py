X, Y, N = map(int, input().split())

x = N % 3
y = N // 3

if X > Y/3:
  print(x*X + y*Y)
else:
  print(X*N)
