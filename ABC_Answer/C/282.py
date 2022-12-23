N = int(input())
S = list(input())

double_cort_cnt = 0
for i in range(N):
  if S[i] == ',':
    if double_cort_cnt % 2 == 0:
      S[i] = "."
  if S[i] == '"':
    double_cort_cnt += 1

print("".join(S))
