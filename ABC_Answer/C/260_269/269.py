from collections import defaultdict


N = int(input())
bitN = bin(N)[2:]

bit1_list = []
i = 0
for bit in reversed(bitN):
  if bit == '1':
    bit1_list.append(i)
  i += 1

ans_dict = defaultdict(list)
all_pattern = len(bit1_list)
for i in range(2 ** all_pattern):
  for j in range(all_pattern):
    if ((i >> j) & 1):
      ans_dict[i].append(j)      

ans_list = []
for k, v in ans_dict.items():
  ans = 0
  for bit in v:
    ans += 2**bit1_list[bit]
  ans_list.append(ans)

ans_list = [0] + ans_list

for ans in ans_list:
  print(ans)