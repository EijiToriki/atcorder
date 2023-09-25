import queue
import math

def calc(a1, b1, a2, b2):
    return math.sqrt((a1-b1)**2 + (a2-b2)**2)


N, D = map(int, input().split())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

patient = set([0])

virus_checker = queue.Queue()
virus_checker.put(0)

while not virus_checker.empty():
    person = virus_checker.get()
    for i in range(N):
        if calc(XY[person][0], XY[i][0], XY[person][1], XY[i][1]) <= D and i not in patient:
            virus_checker.put(i)
            patient.add(i)

for i in range(N):
    if i in patient:
        print('Yes')
    else:
        print('No')
