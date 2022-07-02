N = int(input())
A = [input() for _ in range(N)]

AInt = []
for a in A:
    AIntEle = []
    for ele in a:
        AIntEle.append(int(ele))
    AInt.append(AIntEle)

valList = []
for i in range(N):
    for j in range(N):
        for k in range(8):
            value = 0
            for m in range(N):
                if k == 0:
                    if i+m < N:
                        value += 10**(N-m-1) * AInt[i+m][j]
                    else:
                        value += 10**(N-m-1) * AInt[i+m-N][j]
                if k == 1:
                    value += 10**(N-m-1) * AInt[i-m][j]
                if k == 2:
                    if j+m < N:
                        value += 10**(N-m-1) * AInt[i][j+m]
                    else:
                        value += 10**(N-m-1) * AInt[i][j+m-N]
                if k == 3:
                    value += 10**(N-m-1) * AInt[i][j-m]
                if k == 4:
                    if i+m < N and j+m < N:
                        value += 10**(N-m-1) * AInt[i+m][j+m]
                    elif i+m < N:
                        value += 10**(N-m-1) * AInt[i+m][j+m-N]
                    elif j+m < N:
                        value += 10**(N-m-1) * AInt[i+m-N][j+m]
                    else:
                        value += 10**(N-m-1) * AInt[i+m-N][j+m-N]
                if k == 5:
                    value += 10**(N-m-1) * AInt[i-m][j-m]
                if k == 6:
                    if i+m < N:
                        value += 10**(N-m-1) * AInt[i+m][j-m]
                    else:
                        value += 10**(N-m-1) * AInt[i+m-N][j-m]
                if k == 7:
                    if j+m < N:
                        value += 10**(N-m-1) * AInt[i-m][j+m]
                    else:
                        value += 10**(N-m-1) * AInt[i-m][j+m-N]
                valList.append(value)  

print(max(valList))