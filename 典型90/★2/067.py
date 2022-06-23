import re

def dec_to_nin(N):
    nin_list = []
    while True:
        sho = N // 9
        if sho == 0:
            nin_list.insert(0, str(N))
            break
        else:
            nin_list.insert(0, str(N%9))
            N = sho
    return ''.join(nin_list)


N, K = map(int, input().split())

nin_N = str(N)

for _ in range(K):
    dec_N = int(nin_N, 8)
    nin_N = dec_to_nin(dec_N)
    nin_N = re.sub(r'8', '5', nin_N)

print(nin_N)