p, q = input().split()

dist_dict = {
  'A': 0,
  'B': 3,
  'C': 4,
  'D': 8,
  'E': 9,
  'F': 14,
  'G': 23
}

p_dist = dist_dict[p]
q_dist = dist_dict[q]
ans = abs(p_dist-q_dist)
print(ans)
