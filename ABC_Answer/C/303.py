from collections import defaultdict

N, M, H, K = map(int, input().split())
S = input()
potion = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    potion[(x, y)] += 1

position = [0, 0]
for s in S:
    if s == 'R':
        position = [position[0]+1, position[1]]
    elif s == 'L':
        position = [position[0]-1, position[1]]
    elif s == 'U':
        position = [position[0], position[1]+1]
    elif s == 'D':
        position = [position[0], position[1]-1]
    
    H = H - 1

    if H < 0:
        print('No')
        exit()

    if potion[(position[0], position[1])] > 0 and H < K:
        H = K
        potion[(position[0], position[1])] -= 1
    
print('Yes')