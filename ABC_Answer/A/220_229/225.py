S = input()
S = list(S)
char_cnt = len(set(S))

if char_cnt == 3:
  print(6)
elif char_cnt == 2:
  print(3)
else:
  print(1)