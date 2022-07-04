N = int(input())
A = [input() for _ in range(N)]

AInt = []
for a in A:
    AIntEle = []
    for ele in a:
        AIntEle.append(int(ele))
    AInt.append(AIntEle)

yoko = [1,-1,0,0,1,1,-1,-1]
tate = [0,0,1,-1,1,-1,1,-1]
valList = []
for i in range(N):
    for j in range(N):
        for x, y in zip(yoko, tate):
            value = 0
            for l in range(N):
                x_move = x * l
                y_move = y * l
                value += 10**(N-l-1) * AInt[(i+x_move)%N][(j+y_move)%N]
                
            valList.append(value)  

print(max(valList))