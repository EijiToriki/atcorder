from collections import defaultdict

S = input()
K = int(input())

dot_idx = []
for i, s in enumerate(S):
  if s == '.':
    dot_idx.append(i)
dot_idx_set = set(dot_idx)


if len(dot_idx) <= K:
  print(len(S))
  exit()

left_dict = defaultdict(int)
x_num = 0
for i, s in enumerate(S):
  if i in dot_idx_set:
    left_dict[i] = x_num
    x_num = 0
  if s == 'X':
    x_num += 1

right_dict = defaultdict(int)
x_num = 0
for i, s in enumerate(reversed(S)):
  if len(S)-i-1 in dot_idx_set:
    right_dict[len(S)-i-1] = x_num
    x_num = 0
  if s == 'X':
    x_num += 1

if K == 0:
  ans = 0
  for lv in left_dict.values():
    ans = max(ans, lv)
  for rv in right_dict.values():
    ans = max(ans, rv)
  print(ans)
  exit()

ans = -1
for k in range(len(dot_idx)-K+1):
  left = dot_idx[k]
  right = dot_idx[k+K-1]
  
  most_left = left - left_dict[left]
  most_right = right + right_dict[right]
  ans = max(ans, most_right-most_left+1)
  
print(ans)
