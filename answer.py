def is_ok():
    koma = N-1
    T = int(input())
    rT = T - koma
    if T > rT:
        return True
    else:
        return False

def binary_search_AB(ok, ng):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        print(f'? {ok} {mid} {1} {N}')
        if is_ok():
            ok = mid + 1
        else:
            ng = mid - 1
    return ok

def binary_search_AB(ok, ng):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        print(f'? {1} {N} {ok} {mid}')
        if is_ok():
            ok = mid + 1
        else:
            ng = mid - 1
    return ok


N = int(input())
koma = N-1
A, B, C, D = 1, N, 1, N

i = binary_search_AB(A,B)
j = binary_search_AB(C,D)
print(f'! i j')