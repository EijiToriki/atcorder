def judge(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] == 0:
                    return False
    return True

def rotate(A):
    tempA = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tempA[i][j] = A[N-1-j][i]
    return tempA


N = int(input())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))


if judge(A, B):
    print('Yes')
    exit()

for _ in range(3):
    A = rotate(A)
    if judge(A, B):
        print('Yes')
        exit()

print('No')

