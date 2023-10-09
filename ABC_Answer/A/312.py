def has_chrod_list(chrod):
  if chrod in chord_list:
    return True
  else:
    return False

S = input()
chord_list = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

if has_chrod_list(S):
  print('Yes')
else:
  print('No')