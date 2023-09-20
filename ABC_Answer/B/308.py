from collections import defaultdict

def generate_menu(menu):
  menu_dict = defaultdict(int)
  for dish_idx in range(len(menu)):
    menu_dict[D[dish_idx]] = P[dish_idx + 1]  
  return menu_dict


def calc_bill(eated_list, menu, base_money):
  total = 0
  for eated in eated_list:
    if eated not in menu:
      total += base_money
    else:
      total += menu[eated]
  return total


M, N = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

menu_dict = generate_menu(D)
total = calc_bill(C, menu_dict, P[0])
print(total)