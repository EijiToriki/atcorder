N, K = map(int, input().split())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

pointList = [a-b for a,b in zip(A,B)]   # AとBの差分
pointList.extend(B)

pointList = sorted(pointList, reverse=True)

ansScore = 0
for i, point in enumerate(pointList):
    ansScore += point
    if i+1 == K:
        break

print(ansScore)