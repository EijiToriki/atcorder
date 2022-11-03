from collections import defaultdict

P = list(map(int, input().split()))
alphabet = [chr(i) for i in range(97, 97+26)]

numToAlpha = defaultdict(str)
for i in range(1, 27):
  numToAlpha[i] = alphabet[i-1]

ans = ""
for p in P:
  ans += numToAlpha[p]

print(ans)