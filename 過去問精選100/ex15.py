## 順列全探索

from dis import dis
import itertools
import math

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

town_num_list = [i for i in range(N)]
route_list = list(itertools.permutations(town_num_list))
total_dist = 0

for town_num in route_list:
  dist = 0
  for i in range(len(town_num)-1):
    dist += math.sqrt((x[town_num[i]]-x[town_num[i+1]])**2 + (y[town_num[i]]-y[town_num[i+1]])**2)
  total_dist += dist

route_num = len(route_list)

print(total_dist/route_num)