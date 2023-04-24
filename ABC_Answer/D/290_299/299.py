
N = int(input())

l = 1
r = N
pre_mid = -1
while l < r:
    mid = (l + r) // 2
    if mid == pre_mid:
        break
    pre_mid = mid

    print('? {}'.format(mid), flush=True)
    Si = int(input())
    if Si == 0:
        l = mid
    elif Si == 1:
        r = mid

print('! {}'.format(mid), flush=True)
exit()
