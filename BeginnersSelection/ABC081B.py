N = int(input())
A = list(map(int, input().split()))

result = 0

while True:
  check_odd = [a%2 for a in A]
  if 1 in check_odd:
    break

  A = [a/2 for a in A]
  result += 1

print(result)