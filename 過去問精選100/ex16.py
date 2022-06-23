## 順列全探索
import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

seq_num_list = [i for i in range(1, N+1)]
pm_list = list(itertools.permutations(seq_num_list))

p_index = -1
q_index = -1

for i in range(len(pm_list)):
  if P == pm_list[i]:
    p_index = i+1
  if Q == pm_list[i]:
    q_index = i+1
  if p_index > 0 and q_index > 0:
    break

print(abs(p_index-q_index))
