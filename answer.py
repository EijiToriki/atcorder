N, X = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

min_stage2 = 10**9+1
clear_stage = 0
ans = 0
for i in range(N):
    if clear_stage == 0:
        ans = A[i] + B[i]
        clear_stage = 1
        min_stage2 = B[i]
    else:
        if min_stage2*(X-clear_stage) < A[i] + B[i] + B[i] * (X-clear_stage-1):
            ans += min_stage2*(X-clear_stage)
            print(i)
            break
        else:
            ans += A[i] + B[i]
            if min_stage2 > B[i]:
                min_stage2 = B[i]
            clear_stage += 1

print(ans)
    
