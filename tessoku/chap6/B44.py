N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A_row_idx = [i for i in range(N)]
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A_row_idx[query[1]-1], A_row_idx[query[2]-1] = A_row_idx[query[2]-1], A_row_idx[query[1]-1]
    else:
        print(A[A_row_idx[query[1]-1]][query[2]-1])
