N = int(input())
S = input()

grass = [1]
Bstart = 0
Bend = 0
Bflag = False

for i in range(N-1):
    append_num = 0
    if S[i] == 'A':
        if Bflag == True:
            Bend = i
            Bflag = False
            for j in range(Bend-Bstart+1):
                if j == 0 and grass[Bstart] < Bend-Bstart+1:
                    grass[Bstart] = Bend-Bstart+1
                elif j == 0 and grass[Bstart] >= Bend-Bstart+1:
                    pass
                else:
                    grass[Bstart + j] = Bend-Bstart+1-j
        append_num = grass[i] + 1
    if S[i] == 'B':
        if Bflag == False:
            Bstart = i
            Bflag = True
        append_num = grass[i] - 1
    
    grass.append(append_num)

if Bflag == True:
    Bend = N-1
    Bflag = False
    for j in range(Bend-Bstart+1):
        if j == 0 and grass[Bstart] < Bend-Bstart+1:
            grass[Bstart] = Bend-Bstart+1
        elif j == 0 and grass[Bstart] >= Bend-Bstart+1:
            pass
        else:
            grass[Bstart + j] = Bend-Bstart+1-j 

ans = sum(grass)
print(ans)
