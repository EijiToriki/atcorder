Y = int(input())
a = Y % 4

if a == 1:
  print(Y+1)
elif a == 2:
  print(Y)
elif a == 3:
  print(Y+3)
elif a == 0:
  print(Y+2)