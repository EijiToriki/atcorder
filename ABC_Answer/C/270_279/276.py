N = int(input())
P = list(map(int, input().split()))

sort_first_index = 0
for i in range(1, N):
  if P[i-1] > P[i]:
    sort_first_index = i

change_els = P[sort_first_index:]

near = P[sort_first_index-1]
u_near_max = -1
for cel in change_els:
  if cel > u_near_max and cel < near:
    u_near_max = cel

change_els.append(near)
change_els.remove(u_near_max)

P[sort_first_index-1] = u_near_max
change_els = sorted(change_els, reverse=True)

ans = []
for i in range(sort_first_index):
  ans.append(P[i])

for i in range(len(change_els)):
  ans.append(change_els[i])

print(*ans)