N = int(input())
poemList = []
pointList = []
for i in range(N):
    poem, point = input().split()
    poemList.append(poem)
    pointList.append(int(point))

originalSet = set()

indexMax = -1
maxPoint = 0

for i in range(len(poemList)):
  if poemList[i] not in originalSet:
    originalSet.add(poemList[i])
    if pointList[i] > maxPoint:
      maxPoint = pointList[i]
      indexMax = i

print(indexMax + 1)