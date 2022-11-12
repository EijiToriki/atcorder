from bisect import bisect_left

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

if N == 1:
  print(0)
  exit()

if M == 2:
  print(0)
  exit()

a_groups = []
group = []
for i in range(len(A)-1):
  if A[i+1] - A[i] <= 1:
    group.append(A[i])
    if i == len(A)-2:
      group.append(A[i+1])
  else:
    group.append(A[i])
    a_groups.append(group)
    if i == len(A)-2:
      group = [A[i+1]]
    else:
      group = []
a_groups.append(group)

if len(a_groups) == 1:
  print(0)
  exit()

ans_list = []
if 0 in a_groups[0] and M-1 in a_groups[len(a_groups)-1]:
  for i in range(1, len(a_groups)-1):
    ans_list.append(sum(a_groups[i]))
  ans_list.append(sum(a_groups[0]) + sum(a_groups[len(a_groups)-1]))
else:
  for i in range(len(a_groups)):
    ans_list.append(sum(a_groups[i]))
  
ans = sum(A) - max(ans_list)
print(ans)

