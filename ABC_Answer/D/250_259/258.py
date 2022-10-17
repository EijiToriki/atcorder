N, X = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

min_stage2_time = 10**9+1
ans_list = []
stage12_total = 0
rest_clear_stage = X

for i in range(N):
    if B[i] < min_stage2_time:
        min_stage2_time = B[i]
    stage12_total += A[i] + B[i]
    rest_clear_stage -= 1
    ans_list.append(stage12_total + min_stage2_time * rest_clear_stage)

print(min(ans_list))