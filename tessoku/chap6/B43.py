N, M = map(int, input().split())
A = list(map(int, input().split()))

correct_num = [M] * (N+1)
for a in A:
    correct_num[a] -= 1

for i in range(1, N+1):
    print(correct_num[i])