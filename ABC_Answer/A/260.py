import sys
S = input()

char_dict = {}
for s in S:
  if s in char_dict:
    char_dict[s] += 1
  else:
    char_dict[s] = 1

for s, cnt in char_dict.items():
  if cnt == 1:
    print(s)
    sys.exit()

print(-1)