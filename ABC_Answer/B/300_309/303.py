from collections import defaultdict

N, M = map(int, input().split())
A = []
nakayoshi = defaultdict(set)
for _ in range(M):
    a = list(map(int, input().split()))
    
    for i in range(N):
        if i == 0:
            nakayoshi[a[i]].add(a[i+1])
        elif i == N-1:
            nakayoshi[a[i]].add(a[i-1])
        else:
            nakayoshi[a[i]].add(a[i+1])
            nakayoshi[a[i]].add(a[i-1])


nakayoshi_total = 0
for nakayoshi_set in nakayoshi.values():
    nakayoshi_total += len(nakayoshi_set)

nakayoshi_total = nakayoshi_total // 2

ans = (N * (N-1)) // 2 - nakayoshi_total
print(ans)
