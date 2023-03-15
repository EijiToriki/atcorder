import heapq

N, D = map(int, input().split())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])
XY = sorted(XY, key=lambda x:x[0])

task = []
heapq.heapify(task)
ans = 0
xy_idx = 0
for d in range(1, D+1):
    while True:
        if xy_idx < len(XY) and XY[xy_idx][0] == d:
            heapq.heappush(task, XY[xy_idx][1] * (-1))
            xy_idx += 1
        else:
            break
    if len(task) > 0:
        ans += heapq.heappop(task) * (-1)

print(ans)
