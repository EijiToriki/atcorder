N, K = map(int, input().split())
C = list(map(int, input().split()))

candy_dict = {}

for i in range(K):
    if C[i] not in candy_dict:
        candy_dict[C[i]] = 1
    else:
        candy_dict[C[i]] += 1

ans = len(candy_dict)

for i in range(K, N):
    if C[i] not in candy_dict:
        candy_dict[C[i]] = 1
    else:
        candy_dict[C[i]] += 1

    candy_dict[C[i-K]] -= 1
    if candy_dict[C[i-K]] == 0:
        del candy_dict[C[i-K]]

    if ans < len(candy_dict) :
        ans = len(candy_dict)

print(ans)