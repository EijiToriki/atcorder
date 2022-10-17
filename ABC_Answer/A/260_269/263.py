from collections import defaultdict
import sys

cards = list(map(int, input().split()))

card_dict = defaultdict(int)

for card in cards:
  card_dict[card] += 1


if len(card_dict.keys()) == 2:
  for k,v in card_dict.items():
    if v == 2 or v == 3:
      None
    else:
      print('No')
      sys.exit()
  print('Yes')
else:
  print('No')

