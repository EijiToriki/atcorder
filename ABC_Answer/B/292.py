N, Q = map(int, input().split())
card = [0] * (N+1)
for _ in range(Q):
    query, player = map(int, input().split())
    if query == 1:
        card[player] += 1
    elif query == 2:
        card[player] = 2
    else:
        if card[player] == 2:
            print('Yes')
        else:
            print('No')
