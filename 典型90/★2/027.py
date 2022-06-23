N = int(input())

name_data = set()

for i in range(N):
  S = input()
  if S not in name_data:
    print(i+1)
    name_data.add(S)