from collections import defaultdict

def xC3(x):
    bunbo = 6
    bunshi = x * (x-1) * (x-2)
    return bunshi // bunbo


N = int(input())
A = list(map(int, input().split()))
a_dict = defaultdict(int)

for a in A:
    a_dict[a] += 1

ans = 0
for x in a_dict.values():
    if x >= 3:
        ans += xC3(x)

print(ans)