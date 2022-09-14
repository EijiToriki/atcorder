from math import ceil, log2

W = int(input())

ans = set()

wlog = ceil(log2(W))
for i in range(wlog):
  ans.add(2**i)


for i in range(1, W+1):
  bitN = bin(i)[2:]
  if bitN.count('1') > 3:
    addValue = 0
    for j in range(len(bitN[2:])):
      addValue += 2**(len(bitN[2:])-j-1)
    ans.add(addValue)

print(len(ans))
print(*ans)