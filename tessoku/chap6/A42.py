N, K = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

ans = 0
for hp in range(1, 101):
    for mp in range(1, 101):
        student_num = 0
        for ab in AB:
            if hp <= ab[0] <= hp + K and mp <= ab[1] <= mp + K:
                student_num += 1
        ans = max(ans, student_num)

print(ans)