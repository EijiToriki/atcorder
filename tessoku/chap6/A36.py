N, K = map(int, input().split())
judge_num = K - 2 * (N-1)

if judge_num < 0 or judge_num % 2 == 1:
    print('No')
else:
    print('Yes')
