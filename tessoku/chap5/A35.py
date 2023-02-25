N = int(input())
A = list(map(int, input().split()))

pyramid = [A]
cnt = 0
for i in range(N-2, -1, -1):
    buf = []
    for j in range(1, len(pyramid[cnt])):
        if i % 2 == 0:
            # 太朗
            buf.append(max(pyramid[cnt][j], pyramid[cnt][j-1]))
        else:
            # 次郎
            buf.append(min(pyramid[cnt][j], pyramid[cnt][j-1]))    
    pyramid.append(buf)
    cnt += 1

ans = pyramid[N-1][0]
print(ans)
