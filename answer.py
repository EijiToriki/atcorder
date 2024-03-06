from bisect import bisect_right

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

seller_num = len(A)
buyer_num = len(B)

for sell_idx, a in enumerate(A):
  if sell_idx + 1 < seller_num and A[sell_idx] != A[sell_idx+1]:
    can_buy_num = buyer_num - bisect_right(B, a)
    can_sell_num = sell_idx + 1
    if can_sell_num >= can_buy_num:
      print(a)
      exit()
  elif sell_idx + 1 == seller_num:
    can_buy_num = buyer_num - bisect_right(B, a)
    can_sell_num = sell_idx + 1
    if can_sell_num >= can_buy_num:
      if A[seller_num-1] > B[buyer_num-1]:
        print(B[buyer_num-1]+1)
      else:
        print(A[seller_num-1])
      exit()


