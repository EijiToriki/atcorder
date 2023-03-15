from collections import defaultdict

N = int(input())
num_dict = defaultdict(int)
for _ in range(N):
    a = int(input())
    num_dict[a] += 1

ans = 0
for v in num_dict.values():
    ans += (v * (v-1) // 2)

print(ans)