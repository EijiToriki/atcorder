N = int(input())

num_set = set([i for i in range(1, 2*N + 2)])

print(min(num_set), flush=True)
num_set.remove(min(num_set))

while True:
  aoki_num = int(input())

  if aoki_num == 0:
    break
  else:
    num_set.remove(aoki_num)
    taka_num = min(num_set)
    print(taka_num, flush=True)
    num_set.remove(taka_num)