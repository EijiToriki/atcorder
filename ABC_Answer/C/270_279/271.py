from collections import deque

N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
A_no_kaburi = list(set(A))


kaburi = len(A) - len(A_no_kaburi)
for _ in range(kaburi):
    A_no_kaburi.append(10**9+1)
A = A_no_kaburi.copy()

takahashi_collection = []
manga = deque(A)

i = 1
while len(manga) > 0:    
    current = manga.popleft()
    if current == i:
        takahashi_collection.append(i)
    else:
        if len(manga) >= 2:
            manga.pop()
            manga.pop()
            takahashi_collection.append(i)
            manga.appendleft(current)
        elif len(manga) == 1:
            manga.pop()
            takahashi_collection.append(i)
        else:
            takahashi_collection.append(current)
    i += 1


ans = 0
for i in range(len(takahashi_collection)-1):
    if takahashi_collection[i+1] - takahashi_collection[i] == 1:
        ans = i + 2
    else:
        if takahashi_collection[i] == 1:
            ans = 1
        break

if len(takahashi_collection) == 1 and takahashi_collection[0] == 1:
    ans = 1

print(ans)