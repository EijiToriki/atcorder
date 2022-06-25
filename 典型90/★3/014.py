N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

incomvenence_value = 0

for i in range(N):
    incomvenence_value += abs(A[i] - B[i])

print(incomvenence_value)