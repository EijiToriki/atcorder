X, A, D, N = map(int, input().split())

S = [A+D*i for i in range(10)]

## 値が増えていくパターンだけを考える (8, 5, 2) → (2, 5, 8)
if D < 0:
  fi = A + D*(N-1)
  A = fi
  D = abs(D)

st = A
fi = A + D*(N-1)

ans = 0

## X が数列の中にある場合
if st <= X <= fi:
  if D!=0:
    ans = (X-st) % D
    ans = min(ans, D-ans)
  else:
    ans = 0
## X が数列の中にない場合
else:
  if X < st:
    ans = st - X
  elif X > fi:
    ans = X - fi

print(ans)