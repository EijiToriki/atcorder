N, D = map(int, input().split())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

XY = sorted(XY, key=lambda x:x[0])

ans = 0
used_task = set()

for d in range(1, D+1):
    candidate = []
    for i, xy in enumerate(XY):
        if xy[0] <= d and i not in used_task:
            candidate.append((i, xy[1]))
    try:
        max_val = max(candidate, key=lambda x:x[1])
        ans += max_val[1]
        used_task.add(max_val[0])
    except ValueError:
        pass
        
print(ans)

