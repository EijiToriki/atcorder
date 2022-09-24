Q = int(input())

num_list = []
mark = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        num_list.append([query[1], query[2]])
    else:
        c = query[1]
        ans = 0
        for i in range(mark, len(num_list)):
            if c > num_list[i][1]:
                c = c - num_list[i][1]
                ans += num_list[i][0] * num_list[i][1]
                mark += 1
            elif c < num_list[i][1]:
                num_list[i][1] -= c
                ans += num_list[i][0] * c
                print(ans)
                break
            else:
                ans += num_list[i][0] * num_list[i][1]
                mark += 1
                print(ans)
                break