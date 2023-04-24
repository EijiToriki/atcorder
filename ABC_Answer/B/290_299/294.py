H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

alpha = ["."] + [chr(ord("A")+i) for i in range(26)]

ans = []
for i in range(H):
    buf = []
    for j in range(W):
        buf.append(alpha[A[i][j]])
    ans.append(buf)

for i in range(H):
    print(''.join(ans[i]))