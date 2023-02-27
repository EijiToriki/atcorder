N = int(input())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

ansA = 2
ansB = 2
prevA = AB[0][0]
prevB = AB[0][1]
for i in range(1, N):
    if prevA != AB[i][0] and prevA != AB[i][1]:
        ansA *= 2
    elif prevA == AB[i][0] and prevA != AB[i][1] or prevA != AB[i][0] and prevA == AB[i][1]:
            pass
    else:
        ansA = 0

    if prevB != AB[i][0] and prevB != AB[i][1]:
        ansB *= 2
    elif prevB == AB[i][0] and prevB != AB[i][1] or prevB != AB[i][0] and prevB == AB[i][1]:
        pass
    else:
        ansB = 0

    prevA = AB[i][0]
    prevB = AB[i][1]   

ans = ansA + ansB
print(ans // 2)
