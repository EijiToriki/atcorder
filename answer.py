S = input()

table = [0 for _ in range(2**10)]
table[0] = 1
bit = 0

for i in range(len(S)):
    s = int(S[i])
    bit ^= 2 ** s
    print(bit)
    table[bit] += 1

ans = 0
for t in table:
    ans += t*(t-1) // 2

print(ans)