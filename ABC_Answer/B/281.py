S = input()
alpha = [chr(i) for i in range(65, 65+26)]

head = S[0]
tail = S[-1]
sand = S[1:len(S)-1]

try:
  if len(S) == 8:
    if len(str(int(sand))) == 6 and head in alpha and tail in alpha:
      print('Yes')
    else:
      print('No')
  else:
    print('No')
except ValueError:
  print('No')