S = input()
T = input()

for i in range(len(T)):
  try:
    if S[i] != T[i]:
      ans = i + 1
      break
  except IndexError:
    ans = len(T)

print(ans)