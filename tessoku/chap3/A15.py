from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

A_to_idx = defaultdict(list)
for i, a in enumerate(A):
  A_to_idx[a].append(i)

sortedA = sorted(set(A))
sortA_to_idx = defaultdict(int)
for i, a in enumerate(sortedA):
  sortA_to_idx[a] = i+1

ans = [0] * (N)
for k, v in A_to_idx.items():
  for ele in v:
    ans[ele] = sortA_to_idx[k]

print(*ans)