import heapq

Q = int(input())

pq = []
heapq.heapify(pq)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(pq, query[1])
    elif query[0] == 2:
        min_product = heapq.heappop(pq)
        print(min_product)
        heapq.heappush(pq, min_product)
    else:
        heapq.heappop(pq)

