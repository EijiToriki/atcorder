N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans = (ans ^ A[i])

if ans != 0:
    print('First')
else:
    print('Second')