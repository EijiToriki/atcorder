N = int(input())
A = list(map(int, input().split()))

ans = []
deal_flag = True

for i in range(N-1):
    if abs(A[i]-A[i+1]) != 1:
        if A[i] < A[i+1]:
            for j in range(A[i], A[i+1]):
                ans.append(j)
        else:
            for j in range(A[i], A[i+1], -1):
                ans.append(j)
    else:
        ans.append(A[i])

ans.append(A[N-1])

print(*ans)
