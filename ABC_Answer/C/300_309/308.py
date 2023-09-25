from collections import defaultdict
from decimal import Decimal, getcontext
getcontext().prec = 100


def generate_cointos_rslt(N):
  cointos_rslts = []
  for _ in range(N):
    cointos_dict = defaultdict(Decimal)
    omote, ura = map(Decimal, input().split())
    cointos_dict['omote'], cointos_dict['ura'] = omote, ura
    cointos_rslts.append(cointos_dict)
  return cointos_rslts


def calc_cointos_rate(cointos_rslts):
  success_rate_list = []
  for cointos_rslt in cointos_rslts:
    success_rate = cointos_rslt['omote'] / (cointos_rslt['omote'] + cointos_rslt['ura'])
    success_rate_list.append(success_rate)
  return success_rate_list


def get_cointos_superior_list(success_rate_list):
  sorted_list_idx = sorted(range(len(success_rate_list)),key=success_rate_list.__getitem__, reverse=True)
  sorted_list_idx = [idx + 1 for idx in sorted_list_idx]
  return sorted_list_idx

N = int(input())
cointos_rslts = generate_cointos_rslt(N)
success_rate_list = calc_cointos_rate(cointos_rslts)
superior_list = get_cointos_superior_list(success_rate_list)

print(*superior_list)
