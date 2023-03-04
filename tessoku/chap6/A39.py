MAX_TIME = 86401

N = int(input())
LR = []
for _ in range(N):
    l, r = map(int, input().split())
    LR.append([l, r])

LR = sorted(LR, key=lambda x:(x[1]))
check = [0] * MAX_TIME

ans = 0
for n in range(N):
    ans_flag = True
    for time in range(LR[n][0], LR[n][1]):
        if check[time + 1] == 1:
            ans_flag = False
            break
        check[time + 1] = 1
    if ans_flag:
        ans += 1

print(ans)
