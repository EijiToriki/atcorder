X, Y = map(int, input().split())
ans = []

while True:
    if X == 1 and Y == 1:
        break
    ans.append([X, Y])
    if X > Y:
        X = X - Y
    else:
        Y = Y - X

print(len(ans))
for xy in reversed(ans):
    print(*xy)