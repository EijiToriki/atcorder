import sys
sys.setrecursionlimit(10**6)

a, N = map(int, input().split())
visited = set()
visited.add(N)

def f(n, d):
    next_list = []
    if n%a == 0:
        if n // a not in visited:
            next_list.append([n//a, d+1])
            visited.add(n//a)
            if n // a == 1:
                print(d + 1)
                exit()
                

    if n%10 != 0:
        for i in range(1, len(str(n))):
            new_num = str(n)[-i:] + str(n)[:len(str(n))-i]
            if int(new_num) not in visited:
                next_list.append([int(new_num), d+i])
                visited.add(new_num)


    for next in next_list:
        f(next[0], next[1])




f(N, 0)
