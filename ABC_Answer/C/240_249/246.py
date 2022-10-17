N, K, X = map(int, input().split())
A = list(map(int, input().split()))

sortA = sorted(A, reverse=True)

pricedownA = []

result = 0
for a in sortA:
  price = a
  couponCnt = price // X

  if couponCnt <= K:
    price = price - X * couponCnt
    K = K - couponCnt
  else:
    price = price - X * K
    K = 0

  pricedownA.append(price)

sortPricedownA = sorted(pricedownA, reverse=True)

if len(sortPricedownA) <= K:
  result = 0
elif K != 0:
  result = sum(sortPricedownA[K:])
else:
  result = sum(sortPricedownA)

print(result)
