a, b = map(int, input().split())
MOD = 1000000007

ex_list = [a]
for i in range(30):
    a = (a * a) % MOD
    ex_list.append(a)

b = bin(b)[2:]

ans = 1
for i in range(len(b)):
    if b[len(b)-i-1] == '1':
        ans = ans * ex_list[i] % MOD

print(ans)