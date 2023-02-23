def nimu(n, a):
    val = a[0]
    for i in range(1, n):
        val = (val ^ a[i])
    return val

N, H, W = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

nimu_list = []
for a, b in zip(A, B):
    nimu_list.append(a-1)
    nimu_list.append(b-1)

if nimu(2*N, nimu_list) != 0:
    print('First')
else:
    print('Second')