N = int(input())
S = []
for _ in range(N):
  S.append(input())

first_letter = ["H" ,"D" ,"C" ,"S"]
second_letter = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]

S_set = []
for s in S:
  if s[0] in first_letter and s[1] in second_letter:
    pass
  else:
    print('No')
    exit()
  
  if s in S_set:
    print('No')
    exit()
  S_set.append(s)

print('Yes')
