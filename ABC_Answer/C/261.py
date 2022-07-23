from collections import defaultdict

N = int(input())

str_dict = defaultdict(int)

for i in range(N):
  S = input()
  str_dict[S] += 1

  if str_dict[S] == 1:
    print(S)
  else:
    print(f'{S}({str_dict[S]-1})')