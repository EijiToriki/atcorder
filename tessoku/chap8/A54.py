from collections import defaultdict

Q = int(input())
score_dict  = defaultdict(int)
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        score_dict[query[1]] = int(query[2])
    else:
        print(score_dict[query[1]])

