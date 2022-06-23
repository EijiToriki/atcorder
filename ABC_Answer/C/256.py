def pattern_union(target):
  pat_list = []
  for i in range(1,target):
    for j in range(1,target):
      k = target - i - j
      if k > 0:
        if i+j+k == target:
          pat_list.append([i,j,k])
  return pat_list


hw = list(map(int, input().split()))
h1 = pattern_union(hw[0])
h2 = pattern_union(hw[1])
h3 = pattern_union(hw[2])

ans = 0

for row1 in h1:
  for row2 in h2:
    for row3 in h3:
      column1_sum = row1[0] + row2[0] + row3[0]
      column2_sum = row1[1] + row2[1] + row3[1]
      column3_sum = row1[2] + row2[2] + row3[2]
      if column1_sum == hw[3] and column2_sum == hw[4] and column3_sum == hw[5]:
        ans += 1

print(ans)