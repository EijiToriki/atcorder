N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_idx = 0
b_idx = 0
a_ans = []
b_ans = []
for i in range(1, N+M+1):
    try:
        if A[a_idx] < B[b_idx]:
            a_ans.append(i)
            a_idx += 1
        else:
            b_ans.append(i)
            b_idx += 1
    except IndexError:
        if a_idx == N:
            for j in range(i, N+M+1):
                b_ans.append(j)
        if b_idx == M:
            for j in range(i, N+M+1):
                a_ans.append(j)
        break

print(*a_ans)
print(*b_ans)

