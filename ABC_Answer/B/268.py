S = input()
T = input()

if len(S) > len(T):
  print('No')
else:
  suffix_flag = True
  for i in range(len(S)):
    if S[i] != T[i]:
      suffix_flag = False
      break
  
  if suffix_flag:
    print('Yes')
  else:
    print('No')