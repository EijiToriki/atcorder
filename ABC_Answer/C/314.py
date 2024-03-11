from collections import defaultdict

M, N = map(int, input().split())
S = input()
C = list(map(int, input().split()))

color_dict = defaultdict(list)
for i, c in enumerate(C):
  color_dict[c].append(i)

ans = ["" for _ in range(M)]
for color, idxes in color_dict.items():
  len_idxes = len(idxes)
  for i in range(len_idxes):
    if i+1 == len_idxes:
      ans[idxes[0]] = S[idxes[i]]
    else:
      ans[idxes[i+1]] = S[idxes[i]]

print("".join(ans))

