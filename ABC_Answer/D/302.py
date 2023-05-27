from bisect import bisect_left, bisect_right

def relu(x):
    if x < 0:
        return 0
    else:
        return x

N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = -1
for a in A:
    min_idx = bisect_left(B, relu(a-D))
    max_idx = bisect_right(B, relu(a+D))
    if min_idx != max_idx:
        tmp_idx = max_idx
        while True:
            try:
                if abs(B[tmp_idx]-a) <= D:
                    ans = max(ans, a + B[tmp_idx])
                    break
                else:
                    tmp_idx -= 1
            except IndexError:
                tmp_idx -= 1

print(ans)
