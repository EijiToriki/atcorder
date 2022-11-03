from collections import defaultdict
from operator import itemgetter

X = input()
N = int(input())
S = []
for _ in range(N):
  S.append(input())

ctoi_dict = defaultdict(int)
itoc_dict = defaultdict(str)
for i, x in enumerate(X):
  ctoi_dict[x] = i + 1
  itoc_dict[i+1] = x

S_ctoi = []
for s in S:
  ctoi = []
  for i in range(10):
    try:
      ctoi.append(ctoi_dict[s[i]])
    except IndexError:
      ctoi.append(0)
  S_ctoi.append(ctoi)

S_ctoi = sorted(S_ctoi, key=itemgetter(0,1,2,3,4,5,6,7,8,9))

for s in S_ctoi:
  ans_str = ""
  for i in range(10):
    try:
      ans_str += itoc_dict[s[i]]
    except IndexError:
      pass

  print(ans_str)