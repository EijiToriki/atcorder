L, N1, N2 = map(int, input().split())
row1 = []
for _ in range(N1):
    row1.append(list(map(int, input().split())))

row2 = []
for _ in range(N2):
    row2.append(list(map(int, input().split())))

ans, i, j, n1, n2 = 0, 0, 0, 0, 0
while i < N1 and j < N2:
    if row1[i][0] == row2[j][0]:
        ans += min(n1 + row1[i][1], n2 + row2[j][1]) - max(n1, n2)
    if n1 + row1[i][1] < n2 + row2[j][1]:
        n1 += row1[i][1]
        i += 1
    else:
        n2 += row2[j][1]
        j += 1
print(ans)
