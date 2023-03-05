N = int(input())
A = list(map(int, input().split()))

cnt = [0] * 100

for a in A:
    cnt[a % 100] += 1

ans = 0
for i in range(1, 50):
    ans += cnt[i] * cnt[100-i]

ans += cnt[0] * (cnt[0]-1) // 2
ans += cnt[50] * (cnt[50]-1) // 2

print(ans)