N = int(input())
mizu = [i for i in range(101) if i % 5 == 0]

min = 1000
min_idx = -1
for i in range(len(mizu)):
  if min > abs(mizu[i] - N):
    min = abs(mizu[i] - N)
    min_idx = i

print(mizu[min_idx])