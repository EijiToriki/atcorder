def get_min_dish(dish_list):
  return min(dish_list)

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

min_dish = get_min_dish(D)
drink_and_min_dish = Q + min_dish

ans = min(P, drink_and_min_dish)
print(ans)