from collections import defaultdict

S = input()

alpha = [chr(i) for i in range(65, 65+26)]
alpha_to_num = defaultdict(int)

for i in range(1, len(alpha)+1):
  alpha_to_num[alpha[i-1]] = i

ans = 0
for i, s in enumerate(reversed(S)):
  ans += alpha_to_num[s] * (26 ** i)

print(ans)