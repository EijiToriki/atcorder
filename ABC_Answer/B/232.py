import sys

S = input()
T = input()

if len(S) == 1:
  print('Yes')
else:
  judge_list = []
  for i in range(len(S)):
    s_ord = ord(S[i])
    t_ord = ord(T[i])
    ord_diff = t_ord - s_ord

    if ord_diff < 0:
      ord_diff += 26

    judge_list.append(ord_diff)

    if i == 0:
      continue
    else:
      if judge_list[i-1] != judge_list[i]:
        print('No')
        sys.exit()
  print('Yes')
