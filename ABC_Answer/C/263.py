import itertools

N, M = map(int, input().split())

all_comb = itertools.combinations([i+1 for i in range(M)], N)
for x in all_comb:
  print(' '.join(str(i) for i in x))