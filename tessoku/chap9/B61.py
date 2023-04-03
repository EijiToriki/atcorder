N, M = map(int, input().split())
friend = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a] += 1
    friend[b] += 1

max_friend = max(friend)
ans = friend.index(max_friend)

print(ans)