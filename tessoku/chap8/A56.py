MOD = 2147483647

def hash_value(l, r):
    val = H[r] - (H[l-1] * power100[r-l+1] % MOD)
    if val < 0:
        val += MOD
    return val

N, Q = map(int, input().split())
S = input()

# S の各文字を数値に変換
T = []
for s in S:
    T.append(ord(s)-96)

# 100のn乗
power100 = []
power100.append(1)
for i in range(1, N+1):
    power100.append(100 * power100[i-1] % MOD)

H = []
H.append(0)
for i in range(1, N+1):
    H.append((100 * H[i-1] + T[i-1]) % MOD)


for _ in range(Q):
    a, b, c, d = map(int, input().split())
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print('Yes')
    else:
        print('No')