N = int(input())
A = list(map(int, input().split()))

call_set = set()
for i in range(1, N+1):
    if i not in call_set:
        call_set.add(A[i-1])

n_set = set([i for i in range(1, N+1)])

ans_list = list(n_set - call_set)

print(len(ans_list))
print(*ans_list)
