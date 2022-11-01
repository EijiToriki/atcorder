from collections import defaultdict

X = input()
N = int(input())
S = []
for _ in range(N):
  S.append(input())

seq_dict = defaultdict(int)
for i, x in enumerate(X):
  seq_dict[x] = i + 1


S_ctoi = []
for s in S:
  ctoi = 0
  for i in range(10):
    try:
      print(s, s[i], seq_dict[s[i]])
      ctoi += seq_dict[s[i]] * 10 ** (9-i)
    except IndexError:
      pass
  print(ctoi)
  S_ctoi.append(ctoi)

S_ctoi = sorted(range(len(S_ctoi)), key=S_ctoi.__getitem__)

for i in S_ctoi:
  print(S[i])