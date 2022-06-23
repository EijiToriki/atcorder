from unittest import result


N, A, B = map(int, input().split())

result = 0

for n in range(1,N+1):
  nStr = str(n)
  nArray = list(map(int, nStr))
  nSum = sum(nArray)

  if A <= nSum <= B:
    result += n

print(result)