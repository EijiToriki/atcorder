N, M = map(int, input().split())

node_dict = {}

for i in range(M):
    a, b = map(int, input().split())
    larger_node = max(a,b)
    if larger_node in node_dict:
        node_dict[larger_node] += 1
    else:
        node_dict[larger_node] = 1

print(list(node_dict.values()).count(1))