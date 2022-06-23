## (一応)部分探索
A, B, C, X, Y = map(int, input().split())

if A+B < 2*C:
  price = A*X + B*Y
else:
  fewer_pizza = min(X,Y)
  ## ABピザを買い足せばよい最低ライン
  price = fewer_pizza*2*C
  ## ここからは探索を試みる
  if X > Y:
    for _ in range(X-fewer_pizza):
      if A > 2*C:
        price += 2*C
      else:
        price += A
  elif X < Y:
    for _ in range(Y-fewer_pizza):
      if B > 2*C:
        price += 2*C
      else:
        price += B

print(price)
