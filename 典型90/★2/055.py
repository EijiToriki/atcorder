import itertools
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a in itertools.combinations(A, 5):
    multi_five = a[0]%P * a[1]%P * a[2]%P * a[3]%P * a[4]%P
    if multi_five == Q:
        ans += 1

print(ans)