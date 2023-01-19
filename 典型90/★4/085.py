K = int(input())

divisor = []
for i in range(1, int(K**(1/2))+1):
  if K % i != 0:
    continue
  divisor.append(i)
  if i != K // i:
    divisor.append(K // i)

divisor = sorted(divisor)


ans = 0
for i in range(len(divisor)):
  for j in range(len(divisor)):
    a = divisor[i]
    b = divisor[j]
    c = 0
    if K % (a * b) != 0:
      continue
    c = K // (a * b)
    if a <= b and b <= c:
      ans += 1

print(ans)
